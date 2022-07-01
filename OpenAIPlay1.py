import os
import openai
import json
import pandas as pd
from dotenv import load_dotenv

#LOAD ENV VARIABLES
load_dotenv()
#openai.api_key = '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'
openai.api_key = os.getenv('OPENAI_KEY')

#PROMPT & SETTINGS
prompt_openAI="Questa è una breve storia dell'umanità"
model_openAI="text-davinci-002"
temperature_openAI=0.8
max_tokens_openAI=300

#GET RESPONSE FROM OPENAI
response = openai.Completion.create(model=model_openAI, prompt=prompt_openAI, temperature=temperature_openAI, max_tokens=max_tokens_openAI)

#EFFETTUA IL PARSING DEL JSON DI RITORNO
response_str=str(response) #converte oggetto OpenAI in str
response_dict=json.loads(response_str) #converte la stringa formattata in json in variabile dict
response_text = response_dict['choices'][0]['text']

#VISUALIZZA PROMPT E RISPOSTA

print('Prompt:',prompt_openAI)
print('Risposta:',response_text)
