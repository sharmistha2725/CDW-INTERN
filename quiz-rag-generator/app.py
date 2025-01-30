from dotenv import load_dotenv
import chain
import streamlit as st
import vectordb

load_dotenv()

vectorstore = vectordb.initialize_chroma()

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Page", ["Document Ingestion", "Quiz Generator"])

if page == "Document Ingestion":
    st.title("Upload Documents for Quiz Generation")
    
    uploaded_file = st.file_uploader("Upload a document (PDF, Word, CSV)", 
                                     type=["pdf", "docx", "csv"])

    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

        vectordb.store_pdf_in_chroma(uploaded_file, vectorstore)

else:  
    st.title("Quiz Generator")
    
    with st.form("Quiz Application"):
        num_questions = st.number_input("Number of questions", min_value=1, max_value=20, value=5)
        difficulty = st.selectbox("Select difficulty level", ["Easy", "Medium", "Hard"])
        topic = st.text_input("Enter topic for the quiz (e.g., Maths, Physics)")

        use_rag = st.checkbox("Use RAG for question generation")

        submitted = st.form_submit_button("Generate Quiz")

        if submitted:
            if use_rag:
                st.write("Generating questions using RAG...")
                response = chain.generate_quiz_rag(num_questions, difficulty, topic, vectorstore)

                # Check if the response is a string or list of questions
                if isinstance(response, str):
                    st.write(response)  # If it's a string, just print it
                else:
                    for i, q in enumerate(response, 1):
                        st.write(f"**Question {i}:** {q['question']}")
                        st.radio(f"Choose an option for Question {i}:", q["options"])
            else:
                st.write("Generating standard quiz questions...")
                response = chain.generate_quiz_question(num_questions, difficulty, topic)

                # Check if the response is a string or list of questions
                if isinstance(response, str):
                    st.write(response)  # If it's a string, just print it
                else:
                    for i, q in enumerate(response, 1):
                        st.write(f"**Question {i}:** {q['question']}")
                        st.radio(f"Choose an option for Question {i}:", q["options"])
