# pages/fabric_explorer.py
import streamlit as st
import pandas as pd
from data.fabric_data import fabric_df, get_fabric_types, get_fabrics_by_type

def show_fabric_explorer():
    #st.markdown(css_styles, unsafe_allow_html=True)

    st.title("Fabric Explorer 🔍")
    
    # Sidebar filters
    st.sidebar.subheader("Filters")
    
    # Filter by fabric type
    fabric_type = st.sidebar.selectbox(
        "Select Fabric Type",
        ["All"] + list(get_fabric_types())
    )
    
    # Filter by durability
    durability = st.sidebar.selectbox(
        "Select Durability",
        ["All", "High", "Moderate", "Low"]
    )
    
    # Apply filters
    filtered_df = fabric_df.copy()
    
    if fabric_type != "All":
        filtered_df = filtered_df[filtered_df['Fabric Type'] == fabric_type]
    
    if durability != "All":
        filtered_df = filtered_df[filtered_df['Durability'] == durability]
    
    # Display results
    st.subheader("Fabric Catalog")
    st.dataframe(filtered_df)
    
    # Detailed view
    if not filtered_df.empty:
        selected_fabric = st.selectbox(
            "Select a fabric for detailed information:",
            filtered_df['Fabric Name'].tolist()
        )
        
        if selected_fabric:
            fabric_details = filtered_df[filtered_df['Fabric Name'] == selected_fabric].iloc[0]
            
            st.subheader(f"{selected_fabric} Details")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Type:** {fabric_details['Fabric Type']}")
                st.markdown(f"**Durability:** {fabric_details['Durability']}")
                
            with col2:
                st.markdown(f"**Texture:** {fabric_details['Texture']}")
                st.markdown(f"**Best Use:** {fabric_details['Best Use']}")
