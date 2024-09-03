class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.args = args
        cls.houses_history.append(cls.args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.__str__()

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i + 1)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name}, количество этажей: {self.number_of_floors}")

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print("Введите целое число")

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print("Введите целое число")

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print("Введите целое число")

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print("Введите целое число")

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print("Введите целое число")

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            if isinstance(value, House):
                self.number_of_floors += value.number_of_floors
            return self
        else:
            print("Введите целое число")

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            if isinstance(value, House):
                self.number_of_floors += value.number_of_floors
            return self
        else:
            print("Введите целое число")

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')




h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3

print(House.houses_history)
