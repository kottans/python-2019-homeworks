import http.server
import socketserver
import json
from data_structure import Stack, Linked_list


PORT = 8000

myStack = Stack()
myList = Linked_list()


def ParseRequest(self):
    if not self.headers["Content-Length"]:
        SendResponse(self, 411, "No 'Content-Length' provided")
        return
    content_length = int(self.headers["Content-Length"])
    request = json.loads(self.rfile.read(content_length).decode("UTF-8"))
    return request


def SendResponse(self, responseCode, responsebody=None):
    if responsebody:
        self.send_response(responseCode)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(responsebody, "UTF-8"))
    else:
        self.send_response(responseCode)
        self.end_headers()
    return


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        request = ParseRequest(self)
        if not request:
            return

        if "data_type" in request and "action" in request:
            if request["data_type"] == "stack" and request["action"] == "show":
                SendResponse(self, 200, myStack.show())
            elif request["data_type"] == "linked_list" and request["action"] == "show":
                SendResponse(self, 200, myList.show())
            else:
                SendResponse(
                    self, 400, "Wrong value for 'data_type' or 'action' properties"
                )
        else:
            SendResponse(self, 400, "No 'data_type' or 'action' properties")

    def do_PUT(self):
        request = ParseRequest(self)
        if not request:
            return

        if "data_type" in request and "action" in request:
            if request["data_type"] == "stack":
                if request["action"] == "push" and "value" in request:
                    if request["value"].isalnum():
                        myStack.push(request["value"])
                        SendResponse(self, 200)
                    else:
                        SendResponse(self, 400, "Value is not string or number")

                elif request["action"] == "pop":
                    if len(myStack.stack) >= 1:
                        SendResponse(self, 200, myStack.pop())
                    else:
                        SendResponse(self, 409, "Can't pop from empty stack")
                else:
                    SendResponse(self, 400, "Wrong 'action' value")

            elif request["data_type"] == "linked_list":
                if request["action"] == "insert" and "value" in request:
                    if request["value"].isalnum():
                        if "successor" in request:
                            try:
                                myList.insert(request["value"], request["successor"])
                                SendResponse(self, 200)
                            except:
                                SendResponse(self, 409, "Successor not found")
                        else:
                            myList.insert(request["value"])
                            SendResponse(self, 200)
                    else:
                        SendResponse(self, 400, "Value is not string or number")

                elif request["action"] == "remove" and "value" in request:
                    try:
                        myList.remove(request["value"])
                        SendResponse(self, 200)
                    except:
                        SendResponse(self, 409, "Value not in list")
                else:
                    SendResponse(self, 400, "Wrong 'action' value")
            else:
                SendResponse(self, 400, "Wrong 'data_type' value")
        else:
            SendResponse(self, 400, "No 'data_type' or 'action' in request")


with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
