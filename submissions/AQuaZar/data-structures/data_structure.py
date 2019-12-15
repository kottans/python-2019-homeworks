class Stack:
    def __init__(self, *args):
        self.stack = list(args)

    def show(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data, successor=None):
        if not successor or successor == self.head.data:
            node = Node(data)
            node.next = self.head
            self.head = node
            return True
        current = self.head
        while current:
            if current.next.data == successor:
                node = Node(data)
                node.next = current.next
                current.next = node
                return True
            current = current.next
        # Successor not found
        return False

    def show(self):
        current = self.head
        output = "head ->"
        while current:
            output += f" {current.data} ->"
            current = current.next
        output += " None"
        return output

    def remove(self, data):
        current = self.head
        # if head element has to be removed
        if current.data == data:
            self.head = current.next
            del current
            return True
        # if element in tail
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        # Specified element not in a list
        return False

