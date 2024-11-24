import streamlit as st
from pathlib import Path
import base64

def load_image(image_path):
    """Helper function to load and encode images"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def render_sidebar():
    """Render the sidebar navigation component"""
    with st.sidebar:
        st.title("🧵 Fabric Learning")
        
        # User Profile Section
        st.sidebar.markdown("---")
        col1, col2 = st.columns([1, 3])
        # You can replace this with an actual user image
        col1.markdown("👤")
        with col2:
            st.markdown("### Welcome!")
            st.text("Fabric Explorer")
        st.sidebar.markdown("---")
        
        # Navigation Menu
        selected = st.radio(
            "Navigation",
            options=[
                "🏠 Home",
                "🔍 Fabric Explorer",
                "📋 Project Assistant",
                "📚 Learning Path",
                "📊 Analytics"
            ],
            index=0
        )
        
        # Settings Section
        st.sidebar.markdown("---")
        with st.sidebar.expander("⚙️ Settings"):
            st.checkbox("Dark Mode", value=True)
            st.select_slider(
                "Text Size",
                options=["Small", "Medium", "Large"],
                value="Medium"
            )
        
        # Footer
        st.sidebar.markdown("---")
        st.sidebar.markdown(
            """
            <div style='text-align: center'>
                <small>Made with ❤️ for fabric enthusiasts</small>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        return selected.split(" ")[1]  # Return selected page without emoji