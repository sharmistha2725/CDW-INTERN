from dotenv import load_dotenv
import chain
import streamlit as st

load_dotenv()

def poem_generator_app():
    '''
    Function - Poem generator app

    Return - response poem
    '''
    with st.form("Poem Generator"): 
        topic = st.text_input("Enter topic for the poem")
        submitted = st.form_submit_button("Submit")

        if (submitted) :
            response = chain.generate_poem(topic)
            st.info(response)

 
poem_generator_app()





