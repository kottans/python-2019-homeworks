import requests
import json

url = "http://localhost:8000/"

data = {"data_type": "linked_list", "action": "insert", "value": "Jotaro"}
data = json.dumps(data)
r = requests.put(url, data)
data = {"data_type": "linked_list", "action": "insert", "value": "Joseph"}
data = json.dumps(data)
r = requests.put(url, data)
data = {"data_type": "linked_list", "action": "insert", "value": "Jonathan"}
data = json.dumps(data)
r = requests.put(url, data)
data = {
    "data_type": "linked_list",
    "action": "insert",
    "value": "Joske",
    "successor": "Jotaro",
}
data = json.dumps(data)
r = requests.put(url, data)


data = {"data_type": "linked_list", "action": "show"}
data = json.dumps(data)
r = requests.get(url, data=data)
print(r.content)
