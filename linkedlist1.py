class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtIndex(self, data, index):
        if index == 0:
            self.InsertAtBegin(data)
            return
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return
        if index == 0:
            self.remove_first_node()
            return
        position = 0
        current_node = self.head
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    def remove_node(self, data):
        current_node = self.head
        if current_node is not None and current_node.data == data:
            remove_first_node(current_node)
            return

        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def updateNode(self, data, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            current_node.data = data
        else:
            print("Index not presented")


llist = LinkedList()

llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

print("Node Data:")
llist.printLL()
print("\nRemove First Node:")
llist.remove_first_node()
llist.printLL()
print("\nRemove Last Node:")
llist.remove_last_node()
llist.printLL()
print("\nRemove Node at Index 1:")
llist.remove_at_index(1)
llist.printLL()
print("\nLinked list after removing a node:")
llist.printLL()
print("\nUpdate node Value at Index 0:")
llist.updateNode('z', 0)
llist.printLL()
print("\nSize of linked list:", llist.sizeOfLL())
