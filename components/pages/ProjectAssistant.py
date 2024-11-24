# pages/project_assistant.py
import streamlit as st
from data.fabric_data import fabric_df
from PIL import Image

img = Image.open(r"Fabric-O-Fashion/components/pages/logowhite.png")

def show_project_assistant():
    st.image(img, width=100, use_column_width=False)
    st.title("Project Assistant 📋")

   
    st.markdown("""
    Let's help you find the perfect fabric for your project!
    Fill in the details below, and we'll provide recommendations.
    """)
    
    # Project requirements form
    project_type = st.selectbox(
        "What type of project are you working on?",
        ["Clothing", "Home Decor", "Accessories", "Other"]
    )
    
    durability_needed = st.select_slider(
        "How durable does the fabric need to be?",
        options=["Low", "Moderate", "High"],
        value="Moderate"
    )
    
    texture_preference = st.multiselect(
        "Preferred texture(s)?",
        ["Smooth", "Rough", "Soft"]
    )
    
    if st.button("Get Recommendations"):
        # Filter fabrics based on requirements
        recommendations = fabric_df[
            (fabric_df['Durability'] == durability_needed) &
            (fabric_df['Texture'].isin(texture_preference))
        ]
        
        if not recommendations.empty:
            st.subheader("Recommended Fabrics")
            st.dataframe(recommendations)
            
            # Detailed recommendation
            st.subheader("Top Pick")
            top_pick = recommendations.iloc[0]
            st.markdown(f"""
            We recommend **{top_pick['Fabric Name']}** for your project!
            
            **Why this fabric?**
            - Type: {top_pick['Fabric Type']}
            - Durability: {top_pick['Durability']}
            - Best suited for: {top_pick['Best Use']}
            """)
        else:
            st.warning("No exact matches found. Try adjusting your criteria.")
