class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "-->"
            cur = cur.next
        return out[:-2]

    def getsize(self):
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty")
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value
