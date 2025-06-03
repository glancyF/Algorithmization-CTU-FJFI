MAX_CAPACITY = 10


class Node:
    def __init__(self, key: str, data: any):
        self.key = key
        self.data = data

    def __str__(self):
        return f"{self.key}:{self.data}"


class HashTable:
    def __init__(self):
        self.table = [None] * MAX_CAPACITY
        for i in range(MAX_CAPACITY):
            self.table[i] = []
        self.size = 0

    def hash2(self, key: str) -> int:
        return len(key) % MAX_CAPACITY

    def hash3(self, key: str) -> int:
        res = 0
        for c in key:
            res += ord(c)
        return res % MAX_CAPACITY

    def hash(self, key: str) -> int:
        res = 0
        for i in range(len(key)):
            res += ord(key[i]) * i
        return res % MAX_CAPACITY

    def insert1(self, key: str, data: any) -> bool:
        index = self.hash(key)
        for x in self.table[index]:
            if key == x.key:
                return False
        self.table[index].append(Node(key, data))
        self.size += 1
        return True

    def __str__(self):
        result = ""
        for i in range(MAX_CAPACITY):
            result += f"{i}: "
            for x in self.table[i]:
                result += f"{x.key}:{str(x.data)} "
            result += "\n"
        return result

    def find(self, key: str) -> any:
        index = self.hash(key)
        for x in self.table[index]:
            if key == x.key:
                return x.data
        return None

    def remove(self, key: str) -> bool:
        index = self.hash(key)
        for i in range(len(self.table[index])):
            if key == self.table[index][i].key:
                self.table[index].pop(i)
                return True
        return False
