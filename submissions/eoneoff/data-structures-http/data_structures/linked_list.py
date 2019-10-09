from .node import Node

class LinkedList:
    def __init__(self):
        self._root = None
        self._length = 0

    def __iter__(self):
        current = self._root
        while current:
            yield current
            current = current.next

    def insert(self, value, successor = None):
        if(successor and self._root.value != successor):
            for node in self:
                if node.next and node.next.value == successor:
                    node.next = Node(value, node.next)
                    self._length+=1
                    return
            error_message = f'Value {value} is not in the list'
            raise ValueError(error_message)
        else:
            self._root = Node(value, self._root)
            self._length+=1

    def remove(self, value):
        if self._root.value == value:
            self._root = self._root.next
            self._length-=1
            return
        for node in self:
            if node.next and node.next.value == value:
                node.next = node.next.next
                self._length-=1
                return
        error_message = f'Value {value} is not in the list'
        raise ValueError(error_message)

    def show_list(self):
        return [node.value for node in self]

    def __len__(self):
        return self._length
