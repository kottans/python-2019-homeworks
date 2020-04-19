class LinkedList:
    """
    Linked list is a collection of nodes where each node has two fields:
    - data contains the value to be stored in the node
    - next contains a reference to the next node on the list

    The first node is called the head and the last node must have its
    next reference pointing to None.
    """

    def __init__(self):
        self.head = None

    def insert(self, new_node, successor=None):
        before_head = (self.head is not None and self.head.data == successor)

        if successor is None or before_head:
            new_node.next = self.head
            self.head = new_node
            return

        if not self.head:
            raise Exception('List is empty')

        previous_node = self.head
        for node in self:
            if node.data == successor:
                previous_node.next = new_node
                new_node.next = node
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % successor)

    def remove(self, node_to_remove):
        if not self.head:
            raise Exception('List is empty')

        if self.head.data == node_to_remove:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == node_to_remove:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % node_to_remove)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return ' - '.join(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
