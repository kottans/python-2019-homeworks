import socketserver
import dataStructures
socketserver.TCPServer.allow_reuse_address = True

linkedlist = dataStructures.LinkedList()
stack = dataStructures.Stack()


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = (self.request.recv(1024).strip())
        print("{} wrote:".format(self.client_address))
        x = self.data.decode("utf-8").split()
        if x[0].lower() == 'linkedlist':
            if x[1].lower() == 'insert':
                if len(x) > 3 and x[3].lower() == 'before':
                    linkedlist.insert(x[2], before=x[4])
                    self.request.sendall(b'done')
                else:
                    linkedlist.insert(x[2])
                    self.request.sendall(b'done')

            if x[1].lower() == 'remove':
                linkedlist.remove(str(x[2]))
                self.request.sendall(b'done')

            if x[1].lower() == 'show_list':
                self.request.sendall(str.encode(f'{linkedlist.show_list()}'))

        elif x[0].lower() == 'stack':
            if x[1].lower() == 'push':
                stack.push(x[2])
                print(f'Push {x[2]}')
                self.request.sendall(str.encode(f'Push {x[2]}'))

            if x[1].lower() == 'pop':
                self.request.sendall(str.encode(stack.pop()))

            if x[1].lower() == 'show_data':
                print(s)
                self.request.sendall(str.encode(f'{s}'))
        else:
            self.request.sendall(b'unknown command')


if __name__ == "__main__":
    HOST, PORT = "", 8901

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
