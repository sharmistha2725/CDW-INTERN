from dotenv import load_dotenv
import chain
import streamlit as st

load_dotenv()

def quiz_app():
    """
    Function - Quiz app
    Returns - Quiz question and options
    """
    with st.form("Quiz Application"):
        difficulty = st.selectbox("Select difficulty level", ["Easy", "Medium", "Hard"])
        topic = st.text_input("Enter topic for the quiz (e.g., Maths, Physics)")
        submitted = st.form_submit_button("Submit")

        if submitted:
            question, options = chain.generate_quiz_question(difficulty, topic)
            st.write(f"Question: {question}")
            selected_option = st.radio("Choose an option:", options)
        


quiz_app()
