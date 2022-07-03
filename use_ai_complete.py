from openai_functions import ai_complete #import ai_complete: returns a string with the completion of the prompt

#EXAMPLE 1: SIMPLE USE OF ai_complete FUNCTION WITH SIMPLE PROMPT
'''
print(ai_complete("Il migliore amico dell'uomo è", verbose=True))
print(ai_complete("Il più grande musicista di tutti i tempi è",verbose=True))
'''

#EXAMPLE 2: USE OF ai_complete WITH A PROMPT AND A TRAINING TEXT USED TO EXTEND THE PROMPT (RESTAURANT REVIEWS)
'''
prompt="Text: Locale molto accogliente, ampia selezione di vini, menù con poche portate ma molto ricercate e buone, prezzi alti ma in linea con la qualità del cibo e del servizio."

with open ('prep_reviews.txt', 'r') as f:
    prep = f.read()

extended_prompt=prep+'\n'+prompt

print('REVIEW:\n',prompt,'\n\nTEXT ANALYICS:', ai_complete(extended_prompt, max_tokens=100))
'''

#EXAMPLE 3: LOAD OF A LIST OF PROMPTS FROM A JSON FILE AND A PREPROMPT FROM A TEXT FILE, USE OF THE ai_complete FUNCTION TO COMPLETE EACH PROMPT AND PRINT OUT A NEW JSON FILE WITH PROMPTS AND COMPLETIONS

