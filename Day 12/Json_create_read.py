
import json
data = {'name':'John', 'car':['volvo','Mustang'], 'Children': ['Ann','Billy']}
with open ('data.json', 'w')as f:
    json.dump(data, f)
with open ('data.json', 'r') as f:
    content = json.load(f)
    print("loaded data: ", content)
 