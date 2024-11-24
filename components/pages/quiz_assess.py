import streamlit as st
import google.generativeai as genai
import re
from streamlit_lottie import st_lottie
import requests
import json
import time
import plotly.graph_objects as go
from PIL import Image

img = Image.open(r"Fabric-O-Fashion\\components\\pages\\logowhite.png")

# Configure Gemini AI
genai_model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key="AIzaSyBTcMy5sUwBuD1IJqLtyJVptD7Fdm4sOkI")



def get_default_animation():
    """Return a simple default animation if loading fails"""
    return {
        "v": "5.5.7",
        "fr": 30,
        "ip": 0,
        "op": 60,
        "w": 100,
        "h": 100,
        "nm": "Default Animation",
        "ddd": 0,
        "assets": [],
        "layers": [{
            "ddd": 0,
            "ind": 1,
            "ty": 4,
            "nm": "Circle",
            "sr": 1,
            "ks": {
                "o": {"a": 0, "k": 100},
                "r": {"a": 0, "k": 0},
                "p": {"a": 0, "k": [50, 50, 0]},
                "a": {"a": 0, "k": [0, 0, 0]},
                "s": {"a": 0, "k": [100, 100, 100]}
            },
            "shapes": [{
                "ty": "el",
                "p": {"a": 0, "k": [0, 0]},
                "s": {"a": 0, "k": [50, 50]}
            }]
        }]
    }

def load_confetti_animation():
    """Load confetti celebration animation"""
    url = "https://lottie.host/5668398c-cca3-4a30-8c24-74120a644df8/o972OlRDG0.json"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return get_default_animation()
    except:
        return get_default_animation()

def display_celebration():
    """Display confetti celebration for perfect score"""
    animation = load_confetti_animation()
    
    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h1 style="color: #4CAF50; font-size: 2.5em;">🎉 PERFECT SCORE! 🎉</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st_lottie(
        animation,
        key="celebration_confetti",
        height=300
    )

def generate_question():
    """Generate a single question using Gemini AI"""
    response = genai_model.generate_content(
        "Generate a multiple-choice question about fabric durability with a hint. "
        "Format it as: "
        "Question: <Your question here> "
        "Options: A) <Option1>, B) <Option2>, C) <Option3>, D) <Option4> "
        "Correct Answer: (B) or any correct <option> "
        "Hint: <A helpful hint without revealing the answer>"
    )

    generated_text = response.text.strip()

    try:
        # Extract components
        question_match = re.search(r"Question:\s*(.+?)(?=Options:|$)", generated_text, re.DOTALL)
        options_match = re.search(r"Options:\s*(.+?)(?=Correct Answer:|$)", generated_text, re.DOTALL)
        correct_match = re.search(r"Correct Answer:\s*\(?([A-Da-d])\)?", generated_text)
        hint_match = re.search(r"Hint:\s*(.+?)$", generated_text, re.DOTALL)

        question = question_match.group(1).strip() if question_match else None
        options_text = options_match.group(1).strip() if options_match else None
        correct_answer = correct_match.group(1).lower() if correct_match else None
        hint = hint_match.group(1).strip() if hint_match else "No hint available"

        # Parse options
        options = {}
        if options_text:
            patterns = [
                (r'A\)\s*([^B]+)', 'a'),
                (r'B\)\s*([^C]+)', 'b'),
                (r'C\)\s*([^D]+)', 'c'),
                (r'D\)\s*([^\n,]+)', 'd')
            ]
            
            for pattern, key in patterns:
                match = re.search(pattern, options_text)
                if match:
                    options[key] = match.group(1).strip().rstrip(',').strip()

            if len(options) != 4:
                raise ValueError(f"Found {len(options)} options instead of 4")
        
        if not (question and options and correct_answer):
            raise ValueError("Missing question components")

        return question, options, correct_answer, hint

    except Exception as e:
        st.error(f"Error processing the response: {e}")
        return None, None, None, None

def generate_all_questions(num_questions=5):
    """Generate all questions for the quiz"""
    questions = []
    with st.spinner('Generating challenging questions about fabrics...'):
        for _ in range(num_questions):
            question_data = generate_question()
            if all(question_data):
                questions.append(question_data)
    return questions

def display_questions(questions):
    """Display all questions in the quiz"""
    for i, (question, options, _, hint) in enumerate(questions, 1):
        with st.container():
            st.markdown(f"""
                <div class="question-card">
                    <h3>Question {i}:</h3>
                    <p>{question}</p>
                </div>
            """, unsafe_allow_html=True)
            
            answer = st.radio(
                "Select your answer:",
                options=[
                    f"A) {options['a']}",
                    f"B) {options['b']}",
                    f"C) {options['c']}",
                    f"D) {options['d']}",
                ],
                key=f"question_{i}"
            )
            
            if st.button(f"Show Hint 💡", key=f"hint_{i}"):
                st.markdown(f"""
                    <div class="hint-box">
                        <p><strong>Hint:</strong> {hint}</p>
                    </div>
                """, unsafe_allow_html=True)

def evaluate_answers(questions):
    """Evaluate user answers and calculate score"""
    score = 0
    total_questions = len(questions)
    user_answers = []
    correct_answers = []
    
    for i, (_, _, correct_answer, _) in enumerate(questions, 1):
        user_choice = st.session_state[f"question_{i}"]
        selected_key = user_choice[0].lower()
        user_answers.append(selected_key)
        correct_answers.append(correct_answer)
        
        if selected_key == correct_answer:
            score += 1
    
    return score, total_questions, user_answers, correct_answers

def display_performance_chart(score_history):
    """Display performance history chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=list(range(1, len(score_history) + 1)),
        y=score_history,
        mode='lines+markers',
        name='Score History',
        line=dict(color='#4CAF50', width=3),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title='Your Performance History',
        xaxis_title='Attempt Number',
        yaxis_title='Score',
        plot_bgcolor='#2D2D2D',
        paper_bgcolor='#1E1E1E',
        font=dict(color='#FFFFFF'),
        showlegend=False
    )
    
    st.plotly_chart(fig)

def mainy():
    """Main application function"""
    st.image(img, width=100, use_column_width=False)

    # Initialize session state
    if 'questions' not in st.session_state:
        st.session_state.questions = generate_all_questions()
        st.session_state.submitted = False
        st.session_state.start_time = time.time()
        st.session_state.score_history = []
        st.session_state.attempts = 0
        st.session_state.show_celebration = False

    # Show celebration if perfect score
    if st.session_state.show_celebration:
        display_celebration()

    # Sidebar with statistics
    with st.sidebar:
        st.title("📊 Quiz Statistics")
        st.write(f"Total Attempts: {st.session_state.attempts}")
        if st.session_state.score_history:
            st.write(f"Best Score: {max(st.session_state.score_history)}/5")
            st.write(f"Average Score: {sum(st.session_state.score_history)/len(st.session_state.score_history):.1f}/5")
            display_performance_chart(st.session_state.score_history)

    # Main quiz section
    st.title("🧵 Fabric Knowledge Quiz")
    st.subheader("Test your expertise in fabric durability!")

    # Timer
    if not st.session_state.submitted:
        elapsed_time = int(time.time() - st.session_state.start_time)
        st.markdown(f"""
            <div class="timer">
                Time Elapsed: {elapsed_time//60:02d}:{elapsed_time%60:02d}
            </div>
        """, unsafe_allow_html=True)

    # Display questions
    display_questions(st.session_state.questions)

    # Submit button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📝 Submit Quiz", use_container_width=True):
            st.session_state.submitted = True
            score, total, user_answers, correct_answers = evaluate_answers(st.session_state.questions)
            st.session_state.score_history.append(score)
            st.session_state.attempts += 1
            
            # Display results
            st.markdown(f"""
                <div class="score-card">
                    <h2>Quiz Results</h2>
                    <h3>Your score: {score}/{total} ({(score/total)*100:.1f}%)</h3>
                    <div class="progress-bar" style="width: {(score/total)*100}%;"></div>
                </div>
            """, unsafe_allow_html=True)
            
            # Trigger celebration for perfect score
            if score == total:
                st.session_state.show_celebration = True
                st.rerun()
            
            # Detailed feedback
            st.write("\n### Detailed Feedback:")
            for i, (question, _, correct, _) in enumerate(st.session_state.questions):
                user = user_answers[i]
                is_correct = user == correct
                
                feedback_color = "#4CAF50" if is_correct else "#FF5252"
                st.markdown(f"""
                    <div style="background-color: #2D2D2D; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid {feedback_color}">
                        <p>Question {i+1}:</p>
                        <p>Your answer: {user.upper()}</p>
                        <p>Correct answer: {correct.upper()}</p>
                        <p style="color: {feedback_color}">{'✅ Correct!' if is_correct else '❌ Incorrect'}</p>
                    </div>
                """, unsafe_allow_html=True)

            # Reset button
            if st.button("🔄 Start New Quiz"):
                for key in list(st.session_state.keys()):
                    if key not in ['score_history', 'attempts']:
                        del st.session_state[key]
                st.session_state.show_celebration = False
                st.rerun()

if __name__ == "__main__":
    mainy()
