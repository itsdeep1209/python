def search(self, value):
    current_node = self.head.next

    while current_node is not self.tail:
        if current_node.value is value:
            return current_node
        current_node = current_node.next
    return None

def insert_value(self, node, value):
    spot = Node(value)

    spot.prev = node
    spot.next = node.next
    node.next.prev = spot
    node.next = spot

    return True

def insert_after(self, search_value, value):
    search_node = self.search(search_value)

    return self.insert_value(search_node, value) if None is not search_node else False

def insert_before(self, search_value, value):
    search_node = self.search(search_value)

    return self.insert_value(search_node.prev, value) if None is not search_node else False

def add_to_back(self, value):
    self.insert_value(self.tail.prev, value)

def add_to_front(Self, value):
    self.insert_value(self.head, value)

