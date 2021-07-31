import requests
import json
data=requests.get("https://jsonplaceholder.typicode.com/todos")
ExtractedData=data.json()
li=[]
for i in ExtractedData:
    li.append(i["completed"]==True)
list1=[x for x in li if x=='True' in x]
print(li)