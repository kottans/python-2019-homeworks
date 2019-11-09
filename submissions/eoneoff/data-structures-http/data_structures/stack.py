from .node import Node

class Stack:
    def __init__ (self):
        self._root = None
        self._length = 0

    def push(self, value):
        self._root = Node(value, self._root)
        self._length+=1

    def pop(self):
        if self._length:
            out = self._root.value
            self._root = (self._root or None) and self._root.next
            self._length-=1
            return out
        else: return None

    def __len__(self):
        return self._length
