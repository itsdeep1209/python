class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,value):
        spot = Node(value)

        if self.head is None:
            self.head = spot
        else:
            self.tail.next = spot
            spot.prev = self.tail
        self.tail = spot

    def print_forward(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.prev

dll = DoubleLinkedList()
dll.add(5)
dll.add(1)
dll.add(7)

dll.print_backward()