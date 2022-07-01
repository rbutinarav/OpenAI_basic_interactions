import os
import openai
import json
from dotenv import load_dotenv

#LOAD ENV VARIABLES
load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

#PROMPT & SETTINGS
prompt_openAI="Questa è una breve storia dell'umanità"
model_openAI="text-davinci-002"
temperature_openAI=0.8
max_tokens_openAI=300

#GET RESPONSE FROM OPENAI
response = openai.Completion.create(model=model_openAI, prompt=prompt_openAI, temperature=temperature_openAI, max_tokens=max_tokens_openAI)

#PARSE RESPONSE JSON TO GET TEXT COMPLETION FIELD 
response_str=str(response) #converte oggetto OpenAI in str
response_dict=json.loads(response_str) #converte la stringa formattata in json in variabile dict
response_text = response_dict['choices'][0]['text'] #estrae la completion (choices/0/text)

#VISUALIZE PROMPT AND COMPLETION
print('Prompt:',prompt_openAI)
print('Completion:',response_text)
