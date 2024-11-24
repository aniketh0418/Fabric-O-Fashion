# pages/home.py
import streamlit as st
from PIL import Image

img = Image.open(r"\components\pages\logowhite.png")
def show_home():
    st.image(img, width=100, use_column_width=False)

    st.title("Welcome to Fabric Learning Platform 🧵")
    
    st.markdown("""
    ### Your Gateway to Fabric Knowledge
    
    Discover everything you need to know about different types of fabrics, 
    their properties, and best uses.
    
    #### Features Available:
    
    1. 🔍 **Fabric Explorer**: Browse and search through our comprehensive fabric database
    2. 🤖 **AI Fabric Advisor**: Get personalized Fabric selection advise
    3. 📋 **Project Assistant**: Get recommendations for your specific project needs
    4. 📚 **Learning Path**: Structured learning modules about fabric types and properties
    5. 📊 **Analytics Dashboard**: Visualize fabric data and trends
    6. 📝 **Quiz Assessment**: Take a quiz to test your knalowedge
    
    Get started by selecting a section from the sidebar!
    """)
    
    # Quick Search Section
    st.subheader("Quick Search")
    search_query = st.text_input("Search for a fabric:", "")
    
    if search_query:
        from data.fabric_data import search_fabrics
        results = search_fabrics(search_query)
        if not results.empty:
            st.dataframe(results)
        else:
            st.info("No results found. Try a different search term.")
