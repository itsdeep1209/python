class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        spot = Node(value)

        if self.head is None:
            self.head = spot
            self.tail = spot
        else:
            self.tail.next = spot
            self.tail = spot

    def print(self):
        current = self.head
        while(current is not None):
            print(current.value)
            current = current.next

sll = LinkedList()
sll.add_node(5)
sll.add_node(1)
sll.add_node(7)

sll.print()