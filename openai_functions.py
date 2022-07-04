def ai_complete(prompt='Hello', model='text-davinci-002', temperature=0.2, max_tokens=6, verbose=False):
    """
    Returns a string with the completion of the prompt
    """
    import os
    import openai
    import json
    from dotenv import load_dotenv
    import pandas as pd

    #LOAD ENV VARIABLES
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_KEY')

    response = openai.Completion.create(model=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens)
    response_str=str(response) #converts OpenAI object in str
    response_dict=json.loads(response_str) #converts str in dict
    response_text = response_dict['choices'][0]['text'] #parse text (prompt completion)
    if verbose == True:
        return prompt, response_text
    return response_text

def ai_training ():
    """
    Train a model from json dataset and return the model name
    """
    import os
    import openai
    import json
    from dotenv import load_dotenv
    import pandas as pd

    #LOAD ENV VARIABLES
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_KEY')

    return ('This is a test')

#THESE ARE EXAMPLES OF USE OF THE AI_COMPLETE FUNCTION
#print(ai_complete("Il migliore amico dell'uomo è", verbose=True))
#print(ai_complete("Il più grande musicista di tutti i tempi è",verbose=True))
