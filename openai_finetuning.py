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

    import os

    stream = os.popen(('openai api fine_tunes.create -t ' + 'training_reviews.json' + ' -m davinci'))
    output = stream.read()

    return (output)

print(ai_training())

'''Error: No API key provided. You can set your API key in code using 'openai.api_key = <API-KEY>', or you can set the environment variable OPENAI_API_KEY=<API-KEY>). If your API key is stored in a file, you can point the openai module at it with 'openai.api_key_path = <PATH>'. You 
can generate API keys in the OpenAI web interface. See https://onboard.openai.com for details, or email support@openai.com if you have any questions.'''

