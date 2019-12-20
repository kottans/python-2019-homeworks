import socketserver
socketserver.TCPServer.allow_reuse_address = True


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = (self.request.recv(1024).strip())
        print("{} wrote:".format(self.client_address))
        print(self.data)
        if self.data[0] == b'linkedList':
            self.request.sendall(b'!!yay!!')
        print(self.data.split())
        # just send back the same data, but upper-cased
        #self.request.sendall(str(self.data).encode())

if __name__ == "__main__":
    HOST, PORT = "", 8901

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
