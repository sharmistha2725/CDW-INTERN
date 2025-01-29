from model import create_chat_groq_model
import prompts
import model 
import vectordb
from langchain_core.output_parsers import StrOutputParser

def generate_poem(topic):
    '''
    function to generate poem 

    Args :
    topic(Str) - topic of the poem

    Returns : 
    response.content(str)
    '''
    prompt_template = prompts.poem_generator_prompt()
    llm = create_chat_groq_model()
    chain = prompt_template | llm
    

    response = chain.invoke({
        "topic" : topic
    })
    return response.content


#### RETRIEVAL and GENERATION ####

def generate_poem_rag_chain(topic, vector):
    """
    Creates a RAG chain for retrieval and generation.

    Args:
        topic - topic for retrieval
        vectorstore ->  Instance of vector store 

    Returns:
        rag_chain -> rag chain
    """
    # Prompt
    prompt = prompts.poem_generator_rag_prompt_from_hub()

    # LLM
    llm = model.create_chat_groq_model()

    # Post-processing
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    retriever = vectordb.retrieve_from_chroma(topic, vectorstore=vector)
    # Chain
    rag_chain = prompt| llm | StrOutputParser()

    response = rag_chain.invoke({
        "context" : format_docs(retriever),
        "topic": topic
    })    

    return response
