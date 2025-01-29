from langchain_groq import ChatGroq 

def create_chat_groq():
    """
    Function to initialize chat groq
    
    Returns:
        ChatGroq instance
    """
    return ChatGroq(
        model="mixtral-8x7b-32768",
        temperature=0.7,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
