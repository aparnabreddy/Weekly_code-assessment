import requests
import json
data=requests.get("https://jsonplaceholder.typicode.com/todos")
ExtractedData=data.json()
print(ExtractedData)
li=[]
for x in ExtractedData:
    li.append(x["completed"]==True)
list=[i for i in ExtractedData if i["completed"] ==True]
print(list)