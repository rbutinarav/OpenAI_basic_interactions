'''This is a script to export the data from the database to a csv file.
   Still in development.'''

import os
import openai
import json
from dotenv import load_dotenv
import pandas as pd

#EXPORT TO CSV
prompt_openAI="Il migliore amico dell'uomo è"
response_text="Il cane, il 'gatto'"

#EXPORT TO CSV
prompt_response={'prompt':[prompt_openAI],'completion': [response_text]}
prompt_response_df = pd.DataFrame(data=prompt_response)

prompt_response_df.to_csv('out.zip', encoding="utf-8")
print(prompt_response_df)