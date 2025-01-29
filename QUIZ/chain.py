from model import create_chat_qroq
import prompt 
def generate_poem(topic):
    '''
    function to generate poem 

    Args :
    topic(Str) - topic of the poem

    Returns : 
    response.content(str)
    '''
    prompt_template = prompt.poem_generator_prompt_from_hub()
    llm = create_chat_qroq()

    chain = prompt_template | llm
    

    response = chain.invoke({
        "topic" : topic
    })
    return response.content
