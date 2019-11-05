import http.server
import socketserver
from urllib.parse import urlparse

class Node():
    def __init__(self, value):
        self.value = value
        self.next_val = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.root = None
        self.tail = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            self.tail = node
        else:
            self.root.prev = node
            node.next_val = self.root
            self.root = node

    def insert_before(self, new_value, before_value):
        new_node = Node(new_value)
        if self.root.value == before_value:
            new_node.next_val = self.root
            self.root.prev = new_node
            self.root = new_node
        else:
            current = self.root.next_val
            while current != None and current.value != before_value:
                current = current.next_val
            if current == None:
                return "You wan to insert a new element before the element that doesn't exist!!!"
            current.prev.next_val = new_node
            new_node.next_val = current
            new_node.prev = current.prev
            current.prev = new_node

    def remove(self, value):
        if self.root == None:
            return None
        elif self.root.value == value:
            self.root = self.root.next
            self.root.prev = None
        else:
            current = self.root
            while current and current.value != value:
                current = current.next_val
            if current == None:
                return None
            previous = current.prev
            next_val = current.next_val
            previous.next_val = next_val
            next_val.prev = previous
        return value

    def __str__(self):
        current = self.root
        if current == None:
            return "Empty list!!!"
        res = ""
        while current.next_val != None:
            res += str(current) + " - "
            current = current.next_val
        res += str(current)
        return res

linked_list = LinkedList()

PORT = 8081
IP_address = "127.0.0.1"

class HttpProcessor(http.server.SimpleHTTPRequestHandler):
    def do_PUT(self):
        parametres = urlparse(self.path).query.split("&")
        if len(parametres) == 0:
            self.wfile.write(("Enter the value to insert!!!").encode())
        elif len(parametres) == 1:
            linked_list.insert(parametres[0])
            self.wfile.write(("Insert " + parametres[0]).encode())
        else:
            res = linked_list.insert_before(parametres[0], parametres[1])
            if res == None:
                self.wfile.write(("Insert " + parametres[0] + " before " + parametres[1]).encode())
            else:
                self.wfile.write(res.encode())
    def do_DELETE(self):
        value = str(urlparse(self.path).query)
        if value == "":
            self.wfile.write("Enter the value to insert!!!".encode())
        else:
            res = linked_list.remove(value)
            if res != None:
                self.wfile.write(("Remove " + value[0]).encode())
            else:
                self.wfile.write("There is no such an element!!!".encode())
    def do_GET(self):
        res = str(linked_list)
        if res == "Empty list!!!":
            self.wfile.write(res.encode())
        else:
            self.wfile.write(("Show all: " + res + " will be returned").encode())

with socketserver.TCPServer((IP_address, PORT), HttpProcessor) as httpd:
    httpd.serve_forever()