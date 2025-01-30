from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

def create_chat_groq_model(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
):
    """
    Creates and returns a configured instance of the ChatGroq model.
    """
    return ChatGroq(
        model=model,
        temperature=temperature,  # Set to 0 for predictable output
        max_tokens=max_tokens,
        timeout=timeout,
        max_retries=max_retries,
        cache=False
    )

def create_hugging_face_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Creates and returns a configured instance of the HuggingFace embeddings model.
    """
    return HuggingFaceEmbeddings(model_name=model_name)
