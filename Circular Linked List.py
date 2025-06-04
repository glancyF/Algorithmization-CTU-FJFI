class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    def traverse(self):
        if not self.head:
            print("Empty")
            return
        current = self.head
        while True:
            print(current.data, end='->')
            current = current.next
            if current == self.head:
                break
