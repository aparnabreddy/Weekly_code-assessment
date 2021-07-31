import json
import requests
api = requests.get("https://jsonplaceholder.typicode.com/todos")
extract = api.json()
print(type(extract))
print(extract)

New_list = [x for x in extract if x ['completed']==True]
print(New_list)

#Another method
# complete =[]
# for sub in extract:
#     if sub ['completed'] == True:
#         print(sub)
#         complete.append(sub)
# print(complete)