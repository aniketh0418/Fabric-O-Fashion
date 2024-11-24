import streamlit as st
import sys
sys.path.append('../')
from data.fabric_data import fabric_df, get_fabric_types
from PIL import Image

img = Image.open("components/pages/logowhite.png")

def show_learning_path():
    """
    Display the fabric learning path interface in Streamlit.
    This function handles the main UI and logic for the learning path feature.
    """
    st.image(img, width=100, use_column_width=False)

    st.title("Fabric Learning Path 📚")
    
    # Sidebar for learning path selection
    st.sidebar.header("Learning Modules")
    selected_module = st.sidebar.selectbox(
        "Choose your learning path:",
        ["Beginner", "Intermediate", "Advanced"]
    )
    
    # Main content
    st.header(f"{selected_module} Learning Path")
    
    # Learning progress tracking
    progress = st.progress(0)
    status = st.empty()
    
    if selected_module == "Beginner":
        progress.progress(30)
        status.text("Progress: 30% Complete")
        
        st.subheader("Module 1: Introduction to Fabrics")
        with st.expander("Basic Fabric Types"):
            st.write("Learn about the fundamental types of fabrics:")
            fabric_types = get_fabric_types()
            for fabric_type in fabric_types:
                st.write(f"- {fabric_type}")
                
        with st.expander("Natural vs Synthetic Fibers"):
            st.write("""
            - Natural Fibers: Derived from plants or animals
            - Synthetic Fibers: Man-made materials
            - Pros and cons of each type
            """)
            
        with st.expander("Basic Fabric Care"):
            st.write("""
            - Reading care labels
            - Basic washing instructions
            - Common fabric care mistakes
            """)
            
    elif selected_module == "Intermediate":
        progress.progress(60)
        status.text("Progress: 60% Complete")
        
        st.subheader("Module 2: Advanced Fabric Properties")
        with st.expander("Fabric Properties Deep Dive"):
            st.write("""
            - Durability factors
            - Texture analysis
            - Fabric weight and drape
            """)
            
        with st.expander("Specialized Care Techniques"):
            st.write("""
            - Professional cleaning methods
            - Stain removal techniques
            - Storage best practices
            """)
            
    else:  # Advanced
        progress.progress(90)
        status.text("Progress: 90% Complete")
        
        st.subheader("Module 3: Professional Fabric Knowledge")
        with st.expander("Industry Applications"):
            st.write("""
            - Fashion industry standards
            - Commercial fabric selection
            - Quality assessment techniques
            """)
            
        with st.expander("Sustainability and Innovation"):
            st.write("""
            - Eco-friendly fabrics
            - Innovative textile technologies
            - Future of fabric development
            """)
    
    # Interactive quiz section

    
    # Resources section
    st.header("Additional Resources")
    st.write("""
    - 📚 Recommended reading materials
    - 🎥 Video tutorials
    - 💻 Online workshops
    - 🔬 Practical exercises
    """)
    
    # Download materials button
    if st.button("Download Learning Materials"):
        st.download_button(
            label="Download PDF Guide",
            data=b"Sample PDF content",  # Replace with actual PDF content
            file_name="fabric_guide.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    show_learning_path()
