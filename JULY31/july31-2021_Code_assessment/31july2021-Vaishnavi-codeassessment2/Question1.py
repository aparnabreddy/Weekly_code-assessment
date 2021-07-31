import json
import requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    E=data.json()
    #print(ED)
    List=[]
    TrueData=[i for i in E if i["completed"]==True]
    #lis1=[j["completed"] for j in lis if j['completed']==True ]
    List.append(TrueData)
    print(List)

except:
    print("Try again")

else:
    print("completed = true")

finally:
    print("completed ")