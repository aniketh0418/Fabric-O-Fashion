from pymongo import MongoClient
import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from PIL import Image

img = Image.open(r"\components\pages\logowhite.png")


def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'memory' not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()
    if 'chain' not in st.session_state:
        st.session_state.chain = None
    if 'user_requirements' not in st.session_state:
        st.session_state.user_requirements = {}  # To store user inputs dynamically


def setup_llm():
    """Setup LLM and chain"""
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = "AIzaSyCb1hPRJFjiTwV6a_IUwhvCCE8AbytWNkw"

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.5,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    prompt_template = PromptTemplate.from_template(
        """You are **Fabric-O-Fashion**, a friendly and expert Fabric Advisor powered by advanced AI and trained on a comprehensive fabric dataset. Your sole responsibility is to assist users in choosing the best fabric for their design or garment by understanding their requirements and using the dataset to provide tailored suggestions.

        Start by asking thoughtful and friendly questions to gather details about the user's needs, including:
        1. The type of garment (e.g., shirt, dress, suit).
        2. The occasion or purpose (e.g., casual, formal, athletic, special event).
        3. Climate and season (e.g., summer, winter, humid).
        4. Desired qualities (e.g., softness, durability, breathability, stretch).
        5. Preferred colors or patterns.
        6. Any fabric-related allergies or sensitivities.
        7. Budget or cost constraints (if relevant).

        Use the dataset to suggest the most suitable fabric(s) based on their responses. If the user suggests a specific fabric, verify its suitability using the dataset, either confirming the choice, correcting it if necessary, or suggesting a better alternative. If the fabric is appropriate, provide advice on its ideal use cases to help them make an informed decision.

        Always remain polite, friendly, and supportive, providing clear and practical suggestions. Don't ask all the questions at once, ask them one after the other.

        Current conversation:
        {history}
        
        User's input: {learner_input}
        
        Your response as Fabric-O-Fashion:"""
    )

    return LLMChain(llm=llm, prompt=prompt_template, memory=st.session_state.memory)


def query_fabric_dataset(requirements):
    """Query MongoDB for fabrics based on user requirements"""
    client = MongoClient("mongodb+srv://cluster2024:gcloudgenaidb@cluster2024.8qmtq.mongodb.net/?retryWrites=true&w=majority&appName=cluster2024")  # Replace with your MongoDB connection string
    db = client["Fabric-O-Fashion"] 
    collection = db["fabric"]  

    query = {}
    if "garment_type" in requirements:
        query["garment_type"] = requirements["garment_type"]
    if "occasion" in requirements:
        query["occasion"] = requirements["occasion"]
    if "climate" in requirements:
        query["suitable_for_climate"] = requirements["climate"]
    if "qualities" in requirements:
        query["qualities"] = {"$all": requirements["qualities"]}
    if "allergies" in requirements:
        query["allergenic"] = {"$ne": requirements["allergies"]}
    if "budget" in requirements:
        query["price_range"] = {"$lte": requirements["budget"]}

    results = collection.find(query, {"_id": 0})  # Exclude MongoDB default _id field
    return list(results)


def maino():


    # Initialize session state
    initialize_session_state()

    # Setup LLM if not already setup
    if st.session_state.chain is None:
        st.session_state.chain = setup_llm()

    # header image
    st.image(img, use_column_width=True)

    # Header
    st.header("AI Fabric Advisor", divider="rainbow")
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
        ## About
        Fabric-O-Fashion is your personal AI Fabric Advisor, helping you select the perfect fabric for your designs.
        
        ### How it works:
        1. Enter what you're looking to make.
        2. Engage in a dialogue with the AI and answer its questions.
        3. Receive tailored fabric recommendations.
        
        ### Tips:
        - Be specific about your expectations.
        - Answer questions thoughtfully for better suggestions.
        - Mention any specific fabrics you're considering!
        """)

        # Clear conversation button
        if st.button("Clear Conversation", type="secondary"):
            st.session_state.messages = []
            st.session_state.memory = ConversationBufferMemory()
            st.session_state.chain = setup_llm()
            st.session_state.user_requirements = {}
            st.rerun()

    # Display chat messages
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What is on your mind to make today?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Use AI to ask clarifying questions or provide suggestions
        with st.spinner("Thinking..."):
            response = st.session_state.chain.run(learner_input=prompt)

            # Update user requirements if applicable
            if "garment_type" in prompt.lower():
                st.session_state.user_requirements["garment_type"] = prompt
            elif "climate" in prompt.lower():
                st.session_state.user_requirements["climate"] = prompt
            # Extend this logic to capture other inputs dynamically
            
            # Query MongoDB if enough inputs are collected
            if len(st.session_state.user_requirements) >= 3:  # Example threshold for sufficient info
                fabric_suggestions = query_fabric_dataset(st.session_state.user_requirements)
                if fabric_suggestions:
                    suggestions = "\n".join(
                        [f"- {fabric['name']}: {fabric['description']}" for fabric in fabric_suggestions]
                    )
                    response += f"\n\nBased on your inputs, here are some suitable fabrics:\n{suggestions}"
                else:
                    response += "\n\nSorry, no matching fabrics were found in our database. Please refine your inputs."

        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to update the chat display
        st.rerun()


if __name__ == "__main__":
    main()
