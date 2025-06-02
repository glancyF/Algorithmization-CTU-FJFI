class MainNode:
    def __init__(self, data=None):
        self.data = data
        self.num_predecessors = 0
        self.successor_list = []

    def __str__(self):
        result = f"{self.data}: num_pred: {self.num_predecessors}, succ_list: ["

        for tmp in self.successor_list:
            result += str(tmp.data) + " "
        return result + ']'


class TopoSort:
    def __init__(self):
        self.main_list = []
        self.zero_predecessor_list = []
        self.relations = []

    def set_relations(self, rel):
        self.relations = rel

    def build_graph(self):
        for pair in self.relations:
            self.add_relation(*pair)
        print(self)

    def find_or_add(self, data) -> MainNode:
        for x in self.main_list:
            if x.data == data:
                return x
        tmp = MainNode(data)
        self.main_list.append(tmp)
        return tmp

    def add_relation(self, pred, succ):
        p = self.find_or_add(pred)
        s = self.find_or_add(succ)
        for x in self.main_list:
            print(x.data, sep=' ', end='')
        print()
        p.successor_list.append(s)
        s.num_predecessors += 1

    def __str__(self):
        result = ""
        for tmp in self.main_list:
            result += f"{tmp}\n"
        return result

    def find_zero_pred(self):
        for tmp in self.main_list:
            if tmp.num_predecessors == 0:
                self.zero_predecessor_list.append(tmp)

    def get_sorted(self):
        self.build_graph()
        self.find_zero_pred()
        res = []
        size = len(self.main_list)

        i = 0
        while i < len(self.zero_predecessor_list):
            tmp = self.zero_predecessor_list[i]
            res.append(tmp.data)
            size -= 1
            for succ_temp in tmp.successor_list:
                succ_temp.num_predecessors -= 1
                if succ_temp.num_predecessors == 0:
                    self.zero_predecessor_list.append(succ_temp)
            i += 1

        if size != 0:
            return "Cannot sort (cycle detected)"
        return res


relations = [(1, 5), (1, 3), (3, 2), (3, 4), (5, 2), (6, 3), (2, 4), (2, 7), (6, 5)]

drinks = [("voda", "cola"), ("džus", "pivo"), ("rum", "whisky"), ("cola", "pivo"),
          ("voda", "rum"), ("whisky", "pivo")]

T = TopoSort()
T.set_relations(relations)
result = T.get_sorted()
print(result)

T2 = TopoSort()
T2.set_relations(drinks)
print(T2.get_sorted())
