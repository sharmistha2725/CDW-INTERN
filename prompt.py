from langchain_core.prompts import ChatPromptTemplate

def quiz_generator_prompt():
    """
    Generates a prompt template for quiz generation
    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """
    system_msg = """
        You are a knowledgeable quiz generator assistant. Your role is to create quiz questions on specific topics 
        with appropriate difficulty levels. Follow these rules:
        1. Generate a single quiz question and provide 4 multiple-choice options.
        2. The options should include only one correct answer and three plausible incorrect answers.
        3. Format your response as JSON: 
            {{
                "question": "Your generated question",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "correct": "Correct answer"
            }}
        4. Ensure the question aligns with the topic and difficulty level provided.
    """
    user_msg = "Generate a {difficulty} level quiz question on the topic: {topic}."
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("user", user_msg)
    ])
    return prompt_template
