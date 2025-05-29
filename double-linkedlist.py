class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def remove_from_head(self):
        if not self.head:
            return
        removed_data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return removed_data

    def remove_from_tail(self):
        if not self.tail:
            return
        removed_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return removed_data

    def find(self, value) -> int:
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
    def delete_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.remove_from_head()
                elif current == self.tail:
                    self.remove_from_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.length -= 1
                    return current.data
            current = current.next
        return None

    def insert_at_index(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError
        if index == 0:
            self.add_to_head(value)
        if index == self.length:
            self.add_to_tail(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index):
                current = current.next
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node
            self.length += 1

    def get_by_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.prev
        return current.data
