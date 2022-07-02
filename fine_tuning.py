def ai_training ():
    """
    Train a model from json dataset and return the model name.
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

#THIS IS AN EXAMPLE OF JSON TEXT FOR TRAINING
x = [
    {
    "prompt": "Analizza il sentiment. Ristorante pessimo, non torneremo mai più",
    "completion": "Sentiment: molto negativo"},
    {
    "prompt": "Analizza il sentiment. Servizio molto buono, cibo ottimo",
    "completion": "Sentiment: molto positivo"}
]

print(ai_training())

