# app.py
import streamlit as st
import pandas as pd
from components.pages.Home import show_home
from components.pages.FabricExplorer import show_fabric_explorer
from components.pages.ProjectAssistant import show_project_assistant
from components.pages.learning_path import show_learning_path
from components.pages.Analytics import app
from components.pages.quiz_assess import mainy
from components.pages.AI import maino
from PIL import Image

img = Image.open(r"components\pages\logo.png")

# Configure the app
st.set_page_config(
    page_title="Fabric-O-Fashion",
    page_icon=img,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Create a dictionary with the page names and their corresponding functions
PAGES = {
    "Home 🏠": show_home,
    "Fabric Explorer 🔍": show_fabric_explorer,
    "AI Fabric Advisor 🤖" : maino,
    "Project Assistant 📚": show_project_assistant,
    "Learning Path 💡": show_learning_path,
    "Analytics Dashboard 📊": app,
    "Quiz Assessment ✍" : mainy
    
}

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Display the selected page
PAGES[selection]()