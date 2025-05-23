class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.size = 0

    def add_at_begin(self, data):
        tmp = self.head
        self.head = Node(data, tmp)
        self.size += 1

    def append(self, data):
        self.tail.data = data
        self.tail.next = Node(None)
        self.tail = self.tail.next
        self.size += 1

    def find(self, data) -> Node:
        tmp = self.head

        while tmp.data != data:
            tmp = tmp.next
        if tmp == self.tail:
            return None
        else:
            return tmp

    def add(self, data, node:Node):
        if node == self.tail:
            raise Exception("Out of Index")
        node.next = Node(data,node.next)
        self.size += 1

    def delete(self, node: Node):
        if node.next is None:
            raise Exception("Cannot delete the last node this way.")
        node.data = node.next.data
        node.next = node.next.next
        self.size -= 1

    def delete_index(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        prev = self.head
        for _ in range(index):
            prev = prev.next

        to_delete = prev.next
        prev.next = to_delete.next

        if to_delete == self.tail:
            self.tail = prev

        self.size -= 1

    def __str__(self):
        tmp = self.head
        res = ''
        while tmp != self.tail:
            res += str(tmp)
            tmp = tmp.next
            if tmp != self.tail:
                res += ', '
        return res



seznam = LinkedList()
print(seznam)

seznam.add_at_begin(5)
seznam.add_at_begin(2)
seznam.add_at_begin(6)
seznam.add_at_begin(-100)
print(seznam)

seznam.append(0)
seznam.append(-1)

print(seznam)

seznam2 = LinkedList()
seznam2.append(5)

print(seznam2)

prvek = seznam.find(2)
seznam.add(-100, prvek)
print(seznam)

print("Mazani")
seznam.delete_index(0)
print(seznam)

seznam.delete_index(2)
print(seznam)

seznam.delete_index(4)
print(seznam)
