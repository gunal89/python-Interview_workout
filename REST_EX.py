import requests
import json
d = {
    "userId": 11,
"title": 'gunalMuthu',
"completed": True
}

data_json = json.dumps(d)
headers = {'Content-type': 'application/json'}
response1 = requests.post("https://jsonplaceholder.typicode.com/todos/",data=data_json,headers=headers)
print response1
print response1.content

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print response
print response.content

dl= { "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": False
}
response_del = requests.delete("https://jsonplaceholder.typicode.com/todos/",data = json.dumps(dl),headers = headers)
print response_del
print response_del.content

