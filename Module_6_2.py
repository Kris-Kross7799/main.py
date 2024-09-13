# clasself=None#     head = True
#     _legs=True
#     __arms=True
#     def say_hello(self):
#         print('Здравствуйте!')
#
#     def about(self):
#         print(self.head)
#         print(self._legs)
#         print(self.__arms)
#
# class Student(Human):
#     # def about(self):
#     #     print("Я - студент")
#     pass
#
# human=Human()
# student=Student()
# human.about()
# student.about()


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'black', 'серебристый', 'белый', 'зелёный']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return (f"Модель: {self.__model}")

    def get_horsepower(self):
        return (f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        return (f"Цвет транспорта: {self.__color}")

    def print_info(self):
        print(f"Модель: {self.__model}")
        print(f"Мощность двигателя: {self.__engine_power}")
        print(f"Цвет транспорта: {self.__color}")
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        new_color = new_color.lower()
        # __color_variants=[i.lower() for i in self.__color_variants]
        for i in self.__COLOR_VARIANTS:
            i=i.lower()
            if new_color in self.__COLOR_VARIANTS:
                self.__color = new_color
                return new_color
            else:
                print(f"Нельзя сменить цвет на {new_color}")
                return


class Sedan(Vehicle):
    passenger_limit = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print()
# Проверяем что поменялось
vehicle1.print_info()
