import json
import requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    Extracted_data=data.json()
    Empty_list=[]
    for i in Extracted_data:
        if i ['completed'] == True:
            print(i)
            Empty_list.append(i)
    print(Empty_list)
except:
    print("Something went wrong")


