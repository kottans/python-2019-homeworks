class Stack:
    def __init__(self, *args):
        self.data = list(*args)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def __str__(self):
        return str(self.data)


class Node:
    def __init__(self, data=''):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
        self.firstInList = None
        self.lastInList = None

    def insert(self, data, before=None):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.firstInList = node
            self.lastInList = node
            self.len += 1
        elif before is None:
            self.head = self.lastInList
            self.head.previous = node
            self.head = node
            node.next = self.lastInList
            self.lastInList = self.head
            self.len += 1
        elif before:
            x = self.search(before)
            if x:
                if x.previous is None:
                    self.insert(data)
                else:
                    node.previous = self.head.previous if self.head.previous else None
                    node.next = self.head if self.head else None
                    self.head.previous.next = node
                    self.head.previous = node
                    self.len += 1

    def search(self, data):
        self.head = self.lastInList
        while self.head:
            if self.head.data == data:
                return self.head
            else:
                if self.head.next:
                    self.head = self.head.next
                else:
                    self.lastInList = self.head
                    return

    def remove(self, data):
        self.head = self.lastInList
        while self.head:
            if self.head.data == data:
                if self.head.next is None and self.head.previous is None:
                    self.firstInList = None
                    self.lastInList = None
                elif self.head.next is None:
                    self.head.previous.next = None
                    self.firstInList = self.head.previous
                elif self.head.previous is None:
                    self.head.next.previous = None
                    self.lastInList = self.head.next
                else:
                    self.head.previous.next = self.head.next
                    self.head.next.previous = self.head.previous
                self.len -= 1
            self.head = self.head.next

    def show_list(self):
        answ = []
        self.head = self.lastInList
        while self.head:
            answ.append(self.head)
            self.head = self.head.next
        self.head = self.lastInList
        return print(' - '.join(map(str, answ)))

    def __len__(self):
        return self.len


c1 = LinkedList()
c1.insert('A')
c1.insert('B')
c1.insert('C')
c1.insert('D')
c1.insert('E')
c1.insert('F')
c1.insert('X', before='A')
c1.show_list()
c1.remove('E')
c1.remove('A')
c1.remove('F')
c1.remove('X')
c1.remove('C')
c1.remove('D')
c1.remove('B')
c1.show_list()
print(c1.len)
