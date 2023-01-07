import random

def get_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "What's up?"

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == 'help':
        return "I cannot help you."
    
    return "I don't understand!"