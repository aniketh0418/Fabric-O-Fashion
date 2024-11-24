import streamlit as st

def fabric_card(title, content, image_path=None):
    """
    Creates a styled card component for fabric information
    """
    with st.container():
        st.markdown("""
        <style>
        .fabric-card {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #1E1E1E;
            border: 1px solid #333;
            margin: 0.5rem 0;
        }
        </style>
        """, unsafe_allow_html=True)
        
        with st.container():
            st.markdown(f'<div class="fabric-card">', unsafe_allow_html=True)
            
            # Image if provided
            if image_path:
                st.image(image_path, use_column_width=True)
            
            # Title
            st.markdown(f"### {title}")
            
            # Content
            st.write(content)
            
            st.markdown('</div>', unsafe_allow_html=True)

def info_card(title, value, delta=None):
    """
    Creates a metric card for displaying key information
    """
    st.metric(
        label=title,
        value=value,
        delta=delta
    )