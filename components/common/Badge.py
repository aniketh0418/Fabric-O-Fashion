import streamlit as st

def status_badge(text, status):
    """
    Creates a styled badge component
    Status options: 'success', 'warning', 'error', 'info'
    """
    colors = {
        'success': '#28a745',
        'warning': '#ffc107',
        'error': '#dc3545',
        'info': '#17a2b8'
    }
    
    st.markdown(f"""
        <style>
        .badge-{status} {{
            background-color: {colors[status]};
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 0.875rem;
            font-weight: 600;
            display: inline-block;
        }}
        </style>
        <span class="badge-{status}">{text}</span>
    """, unsafe_allow_html=True)

def property_badge(property_name, value):
    """
    Creates a badge for displaying fabric properties
    """
    st.markdown(f"""
        <style>
        .property-badge {{
            background-color: #2d2d2d;
            color: #ffffff;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.875rem;
            margin: 0.25rem;
            display: inline-block;
            border: 1px solid #444;
        }}
        </style>
        <span class="property-badge">{property_name}: {value}</span>
    """, unsafe_allow_html=True)