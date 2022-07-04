from openai_functions import ai_complete

#EXAMPLE 2: USE OF ai_complete WITH A PROMPT AND A TRAINING TEXT USED TO EXTEND THE PROMPT (RESTAURANT REVIEWS)

prompt="Text: Locale molto accogliente, ampia selezione di vini, menù con poche portate ma molto ricercate e buone, prezzi alti ma in linea con la qualità del cibo e del servizio."

with open ('prep_reviews.txt', 'r') as f:
    prep = f.read()

extended_prompt=prep+'\n'+prompt

print('REVIEW:\n',prompt,'\n\nTEXT ANALYICS:', ai_complete(extended_prompt, max_tokens=100))
