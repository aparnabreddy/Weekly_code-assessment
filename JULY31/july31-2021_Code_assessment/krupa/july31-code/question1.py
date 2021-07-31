import requests
import json 
data=requests.get("https://jsonplaceholder.typicode.com/todos")
edata=data.json()
a=[]
for j in edata:
    a.append(j["completed"]==True) 
li=[x for x in a if x=='True' in x]
print(a)