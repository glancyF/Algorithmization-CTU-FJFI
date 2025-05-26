class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        current = self.root
        while True:
            if obj.data < current.data:
                if current.left is None:
                    current.left = obj
                    return obj
                current = current.left

            elif obj.data > current.data:
                if current.right is None:
                    current.right = obj
                    return obj
                current = current.right
            else:
                return None

    def find(self, data) -> tuple[Node, Node]:
        current_node = self.root
        prev_node = None
        while current_node:
            if current_node.data < data:
                prev_node = current_node
                current_node = current_node.right
            elif current_node.data > data:
                prev_node = current_node
                current_node = current_node.left
            else:
                break
        return current_node, prev_node

    def insert(self, data) -> bool:
        current_node, prev_node = self.find(data)
        if current_node:
            return False
        new_node = Node(data)
        if not prev_node:
            self.root = new_node
            return True
        if prev_node.data < data:
            if prev_node.right is None:
                prev_node.right = new_node
                return True
            else:
                return False

        elif prev_node.data > data:
            if prev_node.left is None:
                prev_node.left = new_node
                return True
            else:
                return False

        return True

    def print_recursive(self, node):
        if not node:
            return
        self.print_recursive(node.left)
        print(node.data, end=' ')
        self.print_recursive(node.right)

    def print(self):
        self.print_recursive(self.root)
        print()

    def print_rek(self, node, level=0):
        if not node:
            return
        self.print_rek(node.left, level + 1)
        print(' ' * 4 * level + "->" + str(node.data))
        self.print_rek(node.right, level + 1)

    def print_tree(self):
        print("Tree:")
        self.print_rek(self.root)

    def remove_in_branch(self, current: Node, prev: Node):
        if not prev:
            self.root = current.left if current.left else current.right
            return
        if prev.left == current:
            prev.left = current.left if current.left else current.right
        else:
            prev.right = current.left if current.left else current.right

    def remove_in_tree(self, current: Node):
        tmp = current.left
        tmp_prev = current
        while tmp.right:
            tmp_prev = tmp
            tmp = tmp.right
        current.data = tmp.data
        if tmp.left:
            self.remove_in_branch(tmp, tmp_prev)
        else:
            self.remove_leaf(tmp, tmp_prev)

    def remove_leaf(self, current: Node, prev: Node):
        if current == self.root:
            self.root = None
            return
        if prev.left == current:
            prev.left = None
        else:
            prev.right = None

    def remove(self, data):
        current, prev = self.find(data)
        if not current:
            return False
        if current.left and current.right:
            self.remove_in_tree(current)
        elif current.left or current.right:
            self.remove_in_branch(current, prev)
        else:
            self.remove_leaf(current, prev)
        return True
