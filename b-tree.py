class BTreeNode:
    def __init__(self, t, leaf):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

    def __str__(self, level=0):
        res = "    " * level + str(self.keys) + "\n"
        for child in self.children:
            res += child.__str__(level + 1)
        return res


class Btree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def search(self, k, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and k == node.keys[i]:
            return (node, i)
        elif node.leaf:
            return None
        else:
            return self.search(k, node.children[i])

    def insert(self, k):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(self.root, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k)

    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)
        parent.keys.insert(i, y.keys[t - 1])
        parent.children.insert(i + 1, z)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def print_tree(self):
        print(self.root)

    def _find_key(self, node, k):
        idx = 0
        while idx < len(node.keys) and node.keys[idx] < k:
            idx += 1
        return idx

    def _get_pred(self, node, idx):
        cur = node.children[idx]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def _get_succ(self, node, idx):
        cur = node.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def _fill(self, node, idx):
        t = self.t
        if idx != 0 and len(node.children[idx - 1].keys) >= t:
            self._borrow_from_prev(node, idx)
        elif idx != len(node.keys) and len(node.children[idx + 1].keys) >= t:
            self._borrow_from_next(node, idx)
        else:
            if idx != len(node.keys):
                self._merge(node, idx)
            else:
                self._merge(node, idx - 1)

    def _borrow_from_prev(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx - 1]
        child.keys.insert(0, node.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        node.keys[idx - 1] = sibling.keys.pop()

    def _borrow_from_next(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        node.keys[idx] = sibling.keys.pop(0)

    def _merge(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys.pop(idx))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        node.children.pop(idx + 1)

    def remove(self, k):
        self._remove(self.root, k)
        if not self.root.keys and not self.root.leaf:
            self.root = self.root.children[0]

    def _remove(self, node, k):
        t = self.t
        idx = self._find_key(node, k)
        if idx < len(node.keys) and node.keys[idx] == k:
            if node.leaf:
                node.keys.pop(idx)
            else:
                if len(node.children[idx].keys) >= t:
                    pred = self._get_pred(node, idx)
                    node.keys[idx] = pred
                    self._remove(node.children[idx], pred)
                elif len(node.children[idx + 1].keys) >= t:
                    succ = self._get_succ(node, idx)
                    node.keys[idx] = succ
                    self._remove(node.children[idx + 1], succ)
                else:
                    self._merge(node, idx)
                    self._remove(node.children[idx], k)
        else:
            if node.leaf:
                return
            flag = (idx == len(node.keys))
            if len(node.children[idx].keys) < t:
                self._fill(node, idx)
            if flag and idx > len(node.keys):
                self._remove(node.children[idx - 1], k)
            else:
                self._remove(node.children[idx], k)


