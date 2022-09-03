__author__  = 'Yatsuha'

import os
import json

file = {'file':os.path.dirname(__file__)}

with open('setting.json','w',encoding='utf-8') as f:
    json_dict = json.dump(file,f)

os.system('PAUSE')
