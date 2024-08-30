
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # self.go_to(new_floor)

    def go_to(self, new_floor):
        for i in range(1,self.number_of_floors+1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                break
            if i == new_floor:
                print(f"Добро пожаловать на {new_floor} этаж!")
            elif i < new_floor:
                print(i)











h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(18)
print()
h2.go_to(5)
