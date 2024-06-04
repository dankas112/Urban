class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors > new_floor > 1:
            for x in range(1, new_floor + 1):
                print(x)
        else:
            print('Такого этажа не существует')


print('ELbrus(example):')
Elbrus = House('ЖК Эльбрус', 30)
print(Elbrus.name)
Elbrus.go_to(35)
print('_______')

print('Input data examples:')
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print('_______')

print('My example:')
matreshki = House('ЖК Матрешки', 9)
matreshki.go_to(3)
matreshki.go_to(99)
