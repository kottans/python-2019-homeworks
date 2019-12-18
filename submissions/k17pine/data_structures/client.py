import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    #s.sendall(b'Hello, world')
    mess = (input())
    if mess.split()[0] == 'exit':
        exit()
    s.sendall(bytes((mess), encoding='utf-8'))
    data = s.recv(1023)
    print('Received:', (data.decode("utf-8")))

