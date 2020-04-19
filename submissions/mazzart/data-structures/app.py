from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import urlparse

from linked_list import LinkedList, Node
from stack import Stack

PORT = 8000

linked_list = LinkedList()
stack = Stack()


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path.replace('/', '') == 'list':
            self._set_headers()
            self.wfile.write(f'Show all: {linked_list}'.encode())

    def do_POST(self):
        parameters = urlparse(self.path)
        if parameters.path.replace('/', '') == 'list':
            items = parameters.query.split('&')
            if len(items) == 1:
                item = items[0].split('=')[1]
                if isinstance(item, (int, float, str)):
                    try:
                        linked_list.insert(Node(item))
                        self._set_headers()
                        self.wfile.write(f'Insert {item}'.encode())
                    except Exception as error:
                        print(error)
            elif len(items) == 2:
                item, successor = items[0].split('=')[1], items[1].split('=')[1]
                if isinstance(item, (int, float, str)):
                    try:
                        linked_list.insert(Node(item), successor)
                        self._set_headers()
                        self.wfile.write(
                            f'Insert {item} before {successor}'.encode())
                    except Exception as error:
                        print(error)
        elif parameters.path.replace('/', '') == 'stack':
            item = parameters.query.split('=')[1]
            if isinstance(item, (int, float, str)):
                stack.push(item)
                self._set_headers()
                self.wfile.write(f'Push {item}'.encode())
            else:
                self.send_response(400)
                self.end_headers()

    def do_DELETE(self):
        parameters = urlparse(self.path)
        if parameters.path.replace('/', '') == 'list':
            item = parameters.query.split('=')[1]
            try:
                response = linked_list.remove(item)
                self._set_headers()
                self.wfile.write(f'Remove {item}'.encode())
            except Exception as error:
                print(error)

        elif parameters.path.replace('/', '') == 'stack':
            response = stack.pop()
            if response == 'Stack is empty':
                self.send_response(204)
                self.end_headers()
            else:
                self._set_headers()
                self.wfile.write(f'Pop item: {response}'.encode())


with TCPServer(("", PORT), HTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nserver stopped")
