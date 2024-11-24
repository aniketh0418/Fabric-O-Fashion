import streamlit as st

def render_footer():
    """Render the footer component"""
    
    # Create footer container
    footer_container = st.container()
    
    with footer_container:
        st.markdown("---")
        
        # Footer content with three columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### Quick Links")
            st.markdown("- [About Us](#)")
            st.markdown("- [Contact](#)")
            st.markdown("- [FAQ](#)")
        
        with col2:
            st.markdown("### Resources")
            st.markdown("- [Documentation](#)")
            st.markdown("- [API Reference](#)")
            st.markdown("- [Community](#)")
        
        with col3:
            st.markdown("### Connect")
            st.markdown("- [Twitter](#)")
            st.markdown("- [LinkedIn](#)")
            st.markdown("- [GitHub](#)")
        
        # Copyright notice
        st.markdown(
            """
            <div style='text-align: center; padding: 20px;'>
                <small>© 2024 Fabric Learning Assistant. All rights reserved.</small>
            </div>
            """,
            unsafe_allow_html=True
        )