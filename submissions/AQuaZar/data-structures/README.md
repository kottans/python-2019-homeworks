# Data Structures API

This application is my solution to practice part of data-structures task during Kottans-backend online course. [Link to the task.](https://github.com/kottans/backend/blob/master/tasks/data-structures.md)

Role of this API is to provide means of interaction with two types of data-structures: stack and linked list. Client can work with data stored on the server's memory. Application accepts two types of requests PUT to change data and GET to receive full view of data-structure. To transfer data from client to server JSON format has to be used as a payload to request, response from server passed as a string.

## Available Data Parameters

### Stack

| Name        | Value              | Description                                                                                                                                       |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PUT**     |
| "data_type" | "stack"            | Specifies that stack data-structure is used                                                                                                       |
| "action"    | "push", "pop"      | Push - adds value specified in "Value" property on top of the stack, pop - removes value from top of the stack and returns it in body of response |
| "value"     | alphanumeric value | Value that will be pushed to the stack                                                                                                            |
| **GET**     |
| "data_type" | "stack"            | Specifies that stack data is shown                                                                                                                |
| "action"    | "show"             | Full view of stack will be provided in body of server response                                                                                    |

### Linked List

| Name        | Value              | Description                                                                                                                                   |
| ----------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **PUT**     |
| "data_type" | "linked_list"      | Specifies that data from linked-list structure is affected                                                                                    |
| "action"    | "insert", "remove" | Insert - value specified in "Value" property inserted as a head of the list and will point to successor, remove - removes value from the list |
| "successor" | alphanumeric value | Optional parameter, if member of list is provided, value specified in "Value" property will be inserted before specified successor            |
| "value"     | alphanumeric value | Value that will be inserted to the linked list                                                                                                |
| **GET**     |
| "data_type" | "linked_list"      | Specifies that linked-list data is shown                                                                                                      |
| "action"    | "show"             | Full view of list will be provided in body of server response                                                                                 |

## Examples

For requests will be used 'requests' python library and 'json' library to serialize data.

    import requests
    import json

    url = "http://localhost:8000/"

    data = {"data_type": "linked_list", "action": "insert", "value": "Jonathan"}
    data = json.dumps(data)
    r = requests.put(url, data)

In this example the PUT request is performed. As a result of request string _"Jonathan"_ will be _inserted_ in _linked list_ hold in local server memory.

To check state of our linked list we can use GET request:

    data = {"data_type": "linked_list", "action": "show"}
    data = json.dumps(data)
    r = requests.get(url, data=data)
    print(r.content)

To check the body of respond, 'content' field is used, as result we get:

> b'head -> Jonathan -> None'

In next example we will push values 1,2,3,4,5 to stack and pop last two

    for i in range(1, 6):
        data = {"data_type": "stack", "action": "push", "value": str(i)}
        data = json.dumps(data)
        r = requests.put(url, data=data)
    for i in range(1, 3):
        data = {"data_type": "stack", "action": "pop"}
        data = json.dumps(data)
        r = requests.put(url, data=data)
        print(r.content)

Server responded with:

> b'5'

> b'4'

Another feature of linked list insertion is to specify successor of inserted node. For example we have such list structure:

> b'head -> Jonathan -> Joseph -> Jotaro -> None'

And we want to insert value "Joske" before "Jotaro", so that "Jotaro" will be successor of "Joske", we have to add optional property "successor" to data.

    data = {"data_type": "linked_list", "action": "insert", "value": "Joske", "successor":"Jotaro"}
    data = json.dumps(data)
    r = requests.put(url, data)

As result we get:

> b'head -> Jonathan -> Joseph -> Joske -> Jotaro -> None'
