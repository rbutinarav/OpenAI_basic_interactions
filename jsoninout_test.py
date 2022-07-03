#LOADS PROMPTS FROM A JSON FILE
import json
import pandas as pd

# Opening JSON file
json_file = open('training.json')

json_dict = json.load(json_file)
print(json_dict)

json_df=pd.DataFrame(json_dict)
#for i in json_dict:
#    print(i['prompt'])

print(json_df['prompt']) 
# Closing file
json_file.close()