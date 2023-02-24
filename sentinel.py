class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class SentinelList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, value):
        spot = Node(value)

        spot.next = self.tail
        spot.prev = self.tail.prev
        self.tail.prev.next = spot
        self.tail.prev = spot

    def add_to_back(self, value):
        spot = Node(value)

        spot.next = self.tail
        spot.prev = self.tail.prev
        self.tail.prev.next = spot

    def add_to_front(self, value):
        spot = Node(value)

        spot.prev = self.head
        spot.next = self.head.next
        self.head.next.prev = spot
        self.head.next = spot


    def print_forward(self):
        current_node = self.head.next
        while current_node is not self.tail:
            print(current_node.value)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail.prev
        while current_node is not self.head:
            print(current_node.value)
            current_node = current_node.prev

sentlist = SentinelList()
sentlist.add(5)
sentlist.add(1)
sentlist.add(7)

sentlist.print_forward()
sentlist.print_backward()