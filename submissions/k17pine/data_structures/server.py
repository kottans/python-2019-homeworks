import socket
import time


def stack_push(arg):
    stack.append(arg)
    return f'{arg} pushed'


def stack_pop():
    if len(stack) == 0:
        return 'Stack is NULL'
    else:
        return stack.pop()


def list_insert(arg):
    try:
        if arg[2] == 'before':
            pos = arr.index(arg[3])
            arr.insert(pos, arg[1])
            return f'{arg[1]} inserted before {arg[3]}'
        if arg[2] == 'after':
            pos = arr.index(arg[3])
            arr.insert(pos+1, arg[1])
            return f'{arg[1]} inserted after {arg[3]}'
    except IndexError:
        arr.insert(len(arr), arg[1])
        return f'{arg[1]} inserted'
    except ValueError:
        return f'There is no {arg[3]} in the list'


def list_remove(arg):
    try:
        arr.remove(arg)
        return f'{arg} removed'
    except ValueError:
        return f'How dare you? {arg} not in list'


def list_show():
    if len(arr) == 0:
        return 'List is empty'
    else:
        ans = ''
        for i in arr:
            if ans == '':
                ans = i
            else:
                ans = ans + ' - ' + i
        return ans


def com(txt):
    x = txt.split()
    try:
        if x[0] == 'push':
            ans = stack_push(x[1])
        if x[0] == 'pop':
            ans = stack_pop()
        if x[0] == 'insert':
            ans = list_insert(x)
        if x[0] == 'remove':
            ans = list_remove(x[1])
        if x[0] == 'show' and x[1] == 'all':
            ans = list_show()
        return ans
    except IndexError:
        return f'Look like you forgot some arguments, lol'


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stack = []
arr = []

s.bind((HOST, PORT))
s.listen(2)  # 2 connections
conn, addr = s.accept()  # conn is client socket
print('Connected by', addr)
while True:
    data = conn.recv(1023)
    new_data = com(data.decode("utf-8"))
    conn.sendall(bytes(new_data, encoding='utf-8'))
