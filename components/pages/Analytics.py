import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from data.fabric_data import FABRIC_DF, FABRIC_TYPES  # Importing data
import pandas as pd

def app():
    css_styles = """
    <style>
       .logo-container {
            width: 100px; /* adjust the width to your liking */
            height: 50px; /* adjust the height to your liking */
            border: 1px solid #ddd; /* add a border around the image */
            padding: 10px; /* add some padding around the image */
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
       .logo-container img {
            width: 100%; /* make the image take up the full width of the container */
            height: auto; /* maintain the aspect ratio of the image */
        }
    </style>
"""

# Create a Streamlit container with the image
    st.markdown(css_styles, unsafe_allow_html=True)
    #st.markdown(f"<img src='{"components\pages\logowhite.png"}'  width='300' height='200'>",unsafe_allow_html=True)


    st.title("Fabric Analytics Dashboard 📊")

    # Sidebar filters
    st.sidebar.header("Filters")
    selected_type = st.sidebar.multiselect(
        "Select Fabric Type",
        options=FABRIC_TYPES,
        default=FABRIC_TYPES[0]
    )

    # Filter data based on selection
    filtered_df = FABRIC_DF[FABRIC_DF['Fabric Type'].isin(selected_type)]

    # Main dashboard layout
    st.subheader("Fabric Type Distribution")
    type_counts = filtered_df['Fabric Type'].value_counts()
    fig_types = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        title="Distribution by Fabric Type"
    )
    st.plotly_chart(fig_types)


    # 📈 Key Performance Indicators Section
    st.markdown("### 📈 Key Performance Indicators")
    durability_map = {'High': 3, 'Moderate': 2, 'Low': 1}

    # Row and Column Layout for Durability Meters
    cols_per_row = 3
    selected_count = len(selected_type)

    if selected_count > 0:
        rows = (selected_count + cols_per_row - 1) // cols_per_row  # Calculate required rows
        for i in range(rows):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                idx = i * cols_per_row + j
                if idx < selected_count:
                    fabric_type = selected_type[idx]
                    type_df = filtered_df[filtered_df['Fabric Type'] == fabric_type]

                    if not type_df.empty:
                        avg_durability = type_df['Durability'].map(durability_map).mean()

                        # Plotly Gauge for Durability
                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=avg_durability,
                            title={"text": f"{fabric_type}"},
                            gauge={
                                "axis": {"range": [1, 3], "tickvals": [1, 2, 3], "ticktext": ["Low", "Moderate", "High"]},
                                "bar": {"color": "green"},
                                "steps": [
                                    {"range": [1, 2], "color": "orange"},
                                    {"range": [2, 3], "color": "yellow"}
                                ],
                            }
                        ))

                        # Display the gauge in the current column
                        cols[j].plotly_chart(fig, use_container_width=True)
                    else:
                        cols[j].warning(f"No data for {fabric_type}")

    else:
        st.warning("No fabric types selected.")

    # Enhanced Texture Distribution
    st.subheader("Texture and Durability Analysis")
    durability_color_map = {
        "High": "green",
        "Moderate": "orange",
        "Low": "red"
    }

    fig_texture_durability = px.bar(
        filtered_df,
        x="Texture",
        y="Durability",  # Map Durability as numeric (1: Low, 2: Moderate, 3: High)
        color="Fabric Type",
        barmode="group",
        title="Durability Across Textures",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_texture_durability, use_container_width=True)

    # Best Use Word Cloud (as a table for now)
    st.subheader("Common Uses Overview")
    use_df = filtered_df[['Fabric Name', 'Best Use']].sort_values('Fabric Name')
    st.dataframe(use_df)

    # Detailed Data Table
    st.subheader("Detailed Fabric Data")
    st.dataframe(filtered_df)

    # Export functionality
    if st.button("Export Data"):
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="fabric_analysis.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    app()
