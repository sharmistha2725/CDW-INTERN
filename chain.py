from model import create_chat_groq
import prompt
import json 

def generate_quiz_question(difficulty, topic):
    """
    Function to generate a quiz question

    Args:
        difficulty (str): Difficulty level (Easy, Medium, Hard)
        topic (str): Topic of the question

    Returns:
        tuple: (question, options)

    Parser :
        change json to text o/p
    """
    prompt_template = prompt.quiz_generator_prompt()
    llm = create_chat_groq()

    chain = prompt_template | llm

    response = chain.invoke({
        "difficulty": difficulty,
        "topic": topic
    })

    print("Raw LLM Response:", response)

    
    try:
        
        content = response.content  
        parsed_response = json.loads(content)  

        question = parsed_response["question"]
        options = parsed_response["options"]

        return question, options
    except (KeyError, json.JSONDecodeError) as e:
        raise ValueError(f"Unexpected response format: {response}") from e
