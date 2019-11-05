import http.server
import socketserver
from urllib.parse import urlparse

stack = []

class HttpProcessor(http.server.SimpleHTTPRequestHandler):
    def do_PUT(self):
        parametres = urlparse(self.path).query
        try:
            stack.append(parametres)
            self.wfile.write(("Push " + parametres).encode())
        except:
            self.wfile.write("Enter the value to push!!!".encode())
    def do_DELETE(self):
        try:
            res = stack.pop()
            self.wfile.write(("Pop item: " + res + " will be returned").encode())
        except:
            self.wfile.write("Stack is empty!!!".encode())

PORT = 8080
IP_address = "127.0.0.1"

with socketserver.TCPServer((IP_address, PORT), HttpProcessor) as httpd:
    httpd.serve_forever()