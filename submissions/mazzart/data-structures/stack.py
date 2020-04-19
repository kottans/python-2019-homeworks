class Stack:
    """
    Stack is a data structure that stores items in LIFO manner
    """

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return 'Stack is empty'
