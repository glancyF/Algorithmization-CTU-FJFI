class Equipment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.id})"


class Furniture(Equipment):
    def __init__(self, id, name, legs):
        super().__init__(id, name)
        self.legs = legs

    def __str__(self):
        return super().__str__() + f" legs:{self.legs}"


class Electronics(Equipment):
    def __init__(self, id, name, power):
        super().__init__(id, name)
        self.power = power

    def __str__(self):
        return super().__str__() + f" power:{self.power}"


class WashingMachine(Electronics):
    def __init__(self, id, name, power, weight):
        super().__init__(id, name, power)
        self.weight = weight

    def __str__(self):
        return super().__str__() + f" weight: {self.weight}"


class Household():
    def __init__(self):
        self.equipments = {}

    def add(self, eq=Equipment):
        if eq.id in self.equipments:
            raise Exception("Already exists!")
        self.equipments[eq.id] = eq

    def __str__(self):
        res = ''
        for id, eq in self.equipments.items():
            res += eq.__str__() + "\n"
        return res

    def delete(self, id):
        if id not in self.equipments:
            raise Exception("Object with this id dont exists")
        del self.equipments[id]


e1 = Equipment(1, "Koberec")
e2 = Furniture(2, "Skrin", 4)
e3 = Electronics(3, "TV", "100")
e4 = WashingMachine(4, "Pracka", 500, 50)

print(e1, e2, e3, e4)

house = Household()
try:
    house.add(e1)
    house.add(e2)
    house.add(e3)
    house.add(e4)
except Exception as e:
    print(e)

print(house)

try:
    house.add(e1)
except Exception as e:
    print(e)

try:
    house.delete(2)
    house.delete(2)
except Exception as e:
    print(e)

print(house)
