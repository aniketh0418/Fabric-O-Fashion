import streamlit as st

def render_header(page_title: str):
    """Render the header component with search and notifications"""
    
    # Create header container
    header_container = st.container()
    
    with header_container:
        col1, col2, col3 = st.columns([3, 2, 1])
        
        # Page title and breadcrumb
        with col1:
            st.title(page_title)
            st.markdown(f"Home > {page_title}")
        
        # Search bar
        with col2:
            search_query = st.text_input(
                "Search fabrics...",
                placeholder="Search by name, type, or use...",
                label_visibility="collapsed"
            )
        
        # Notification and profile section
        with col3:
            st.markdown(
                """
                <div style='text-align: right'>
                    <span style='font-size: 1.5em'>🔔</span>
                    <span style='font-size: 1.5em'>👤</span>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        return search_query