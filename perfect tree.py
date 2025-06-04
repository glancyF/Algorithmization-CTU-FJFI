class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTee:
    def perfectBinaryTree(self, depth):
        if depth == 0:
            return TreeNode(0)

        queue = []
        i = 0
        root = TreeNode(i)
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)

            i += 1
            if i > depth:
                break
            else:
                for j in range(size):
                    node = queue.pop(0)
                    node.left = TreeNode(i)
                    node.right = TreeNode(i)
                    queue.append(node.left)
                    queue.append(node.right)
        return root

    def inOrderTraversal(self, node):
        if node is None:
            return
        self.inOrderTraversal(node.left)
        print(node.val, end=" ")
        self.inOrderTraversal(node.right)
