import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import json
from datetime import datetime
import os


# st.set_page_config(
#     page_title="Fashion Design Analyzer",
#     page_icon="👗",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# Custom CSS for advanced styling
st.markdown("""
    <style>
    .main {
        background-color: #0f1116;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #ff4b8d;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff1f6d;
        transform: translateY(-2px);
    }
    .css-1d391kg {
        background-color: #171b21;
    }
    .stTextInput>div>div>input {
        background-color: #1e232a;
        color: white;
        border: 1px solid #2e353e;
    }
    .upload-box {
        border: 2px dashed #ff4b8d;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
    }
    .feedback-box {
        background-color: #1e232a;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Gemini API
def initialize_gemini():
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        return genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.9,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            }
        )
    except Exception as e:
        st.error(f"Error initializing Gemini API: {str(e)}")
        return None

# Function to prepare image for Gemini API
def prepare_image(uploaded_file):
    try:
        # Read the image using PIL
        image = Image.open(uploaded_file)
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Create a bytes buffer
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # Create Gemini-compatible image data
        image_data = {
            "mime_type": "image/png",
            "data": img_byte_arr.getvalue()
        }
        
        return image_data
    except Exception as e:
        st.error(f"Error preparing image: {str(e)}")
        return None
ANALYSIS_PROMPT = """
You are an expert fashion design consultant with deep knowledge in:
- Color theory and combinations
- Fabric selection and textures
- Silhouette and proportion
- Design elements and principles
- Current fashion trends
- Sustainability in fashion
- Technical construction

Analyze the provided design image and provide detailed feedback in the following areas:

1. Overall Design Concept:
   - Uniqueness and creativity
   - Target market suitability
   - Seasonal appropriateness

2. Technical Analysis:
   - Construction techniques
   - Pattern making suggestions
   - Material recommendations
   - Finishing details

3. Aesthetic Elements:
   - Color harmony and balance
   - Proportion and silhouette
   - Texture combinations
   - Design details

4. Market Viability:
   - Commercial potential
   - Target demographic
   - Price point positioning
   - Production scalability

5. Sustainability Considerations:
   - Material sustainability
   - Production efficiency
   - Lifecycle assessment
   - Circular fashion potential

6. Specific Improvements:
   - Provide 3-5 concrete suggestions for enhancement
   - Explain the reasoning behind each suggestion
   - Include technical implementation guidance

Please provide constructive, actionable feedback that will help the student improve their design while maintaining their creative vision.
"""
def analyze_design(uploaded_file, model):
    try:
        # Prepare the image for Gemini API
        image_data = prepare_image(uploaded_file)
        if not image_data:
            return "Error: Could not prepare image for analysis"

        # Generate content with prepared image
        response = model.generate_content([
            image_data,
            "You are a fashion design mentor helping students improve their designs.",
            ANALYSIS_PROMPT
        ])
        return response.text
    except Exception as e:
        return f"Error analyzing design: {str(e)}"

def save_feedback(uploaded_file, feedback):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    feedback_dir = "design_feedback"
    
    if not os.path.exists(feedback_dir):
        os.makedirs(feedback_dir)
        
    # Save feedback
    feedback_data = {
        "timestamp": timestamp,
        "feedback": feedback
    }
    
    with open(f"{feedback_dir}/feedback_{timestamp}.json", "w") as f:
        json.dump(feedback_data, f)
    
    # Save image
    try:
        img = Image.open(uploaded_file)
        img.save(f"{feedback_dir}/design_{timestamp}.png")
    except Exception as e:
        st.warning(f"Could not save image: {str(e)}")

def mainimg():
    # Sidebar setup
    with st.sidebar:
        st.title("🎨 Design Analysis Settings")
        st.markdown("---")
        
        analysis_focus = st.multiselect(
            "Analysis Focus Areas",
            ["Technical Construction", "Color Theory", "Market Viability", 
             "Sustainability", "Trend Alignment", "Production Feasibility"],
            default=["Technical Construction", "Color Theory"]
        )
        
        detail_level = st.select_slider(
            "Feedback Detail Level",
            options=["Basic", "Standard", "Detailed", "Comprehensive"],
            value="Detailed"
        )
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
        This AI-powered tool helps fashion design students analyze and improve their designs
        through professional feedback and suggestions.
        """)

    # Main content
    st.title("👗 Fashion Design Analyzer")
    st.markdown("### Upload your design for professional analysis")

    # File upload with clear instructions
    st.markdown("""
        #### Upload Requirements:
        - Supported formats: PNG, JPG, JPEG
        - Clear, well-lit images
        - Design should be clearly visible
        - Preferably on a neutral background
    """)
    
    uploaded_file = st.file_uploader(
        "Choose a design image file", 
        type=["png", "jpg", "jpeg"],
        help="Upload a clear image of your fashion design"
    )

    if uploaded_file:
        try:
            # Display upload success and image preview
            st.success("Image successfully uploaded!")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.image(uploaded_file, caption="Uploaded Design", use_column_width=True)
                
            with col2:
                st.markdown("### Design Details")
                design_name = st.text_input("Design Name", "Untitled Design")
                design_category = st.selectbox(
                    "Category",
                    ["Casual Wear", "Formal Wear", "Street Style", "Avant-Garde", 
                     "Sustainable Fashion", "Accessories", "Other"]
                )
                target_market = st.multiselect(
                    "Target Market",
                    ["Youth", "Young Professional", "Luxury", "Mass Market", 
                     "Sustainable Conscious", "Special Occasion"],
                    default=["Young Professional"]
                )

            if st.button("Analyze Design", key="analyze"):
                with st.spinner("Analyzing your design... This may take a moment."):
                    model = initialize_gemini()
                    if model:
                        # Reset file position before analysis
                        uploaded_file.seek(0)
                        feedback = analyze_design(uploaded_file, model)
                        
                        # Display feedback in an organized way
                        st.markdown("## Design Analysis Results")
                        
                        # Create tabs for different sections of feedback
                        tabs = st.tabs([
                            "Overall Analysis", 
                            "Technical Details", 
                            "Recommendations"
                        ])
                        
                        feedback_sections = feedback.split("\n\n")
                        
                        with tabs[0]:
                            st.markdown("### Overall Design Analysis")
                            st.markdown(feedback_sections[0] if len(feedback_sections) > 0 else "No analysis available")
                            
                        with tabs[1]:
                            st.markdown("### Technical Details")
                            st.markdown(feedback_sections[1] if len(feedback_sections) > 1 else "No technical details available")
                            
                        with tabs[2]:
                            st.markdown("### Improvement Recommendations")
                            st.markdown(feedback_sections[2] if len(feedback_sections) > 2 else "No recommendations available")
                        
                        # Save feedback (reset file position first)
                        uploaded_file.seek(0)
                        save_feedback(uploaded_file, feedback)
                        
                        # Action buttons
                        col1, col2 = st.columns(2)
                        with col1:
                            st.download_button(
                                "Download Analysis",
                                feedback,
                                file_name=f"design_analysis_{design_name}.txt",
                                mime="text/plain"
                            )
                        with col2:
                            if st.button("Save to Portfolio"):
                                st.success("Analysis saved to your portfolio!")
                                
        except Exception as e:
            st.error(f"An error occurred while processing your design: {str(e)}")
            st.markdown("Please try uploading your image again or contact support if the issue persists.")

    else:
        # Placeholder content when no image is uploaded
        st.markdown("""
            <div class="upload-box">
                <h3>📤 Upload Your Design</h3>
                <p>Upload a clear image of your fashion design to receive professional feedback</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Feature highlights
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                ### 🎯 Professional Analysis
                Get detailed feedback on construction, aesthetics, and market viability
            """)
            
        with col2:
            st.markdown("""
                ### 💡 Improvement Suggestions
                Receive actionable suggestions to enhance your design
            """)
            
        with col3:
            st.markdown("""
                ### 📊 Technical Insights
                Understanding pattern making, materials, and production feasibility
            """)

if _name_ == "_main_":
    mainimg()
