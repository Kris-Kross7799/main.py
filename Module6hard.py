import math


class Figure:
    sides_count = 0

    def __init__(self, color: list[int], *sides: int):
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color=(0,0,0)
        if len(sides) == self.sides_count:  # проверка длины списка sides и количества сторон фигуры
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.filled = True



    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255

    def set_color(self, r, g, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        return all(isinstance(i, int) and i > 0 for i in new_sides)

    def get_sides(self):
        return (self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = list(sides)
        # if len(sides) == self.sides_count:
        #     self.__sides = sides
        # else:
        #     self.__sides = [1] * self.sides_count
        self.radius = self.sides[0] / (2 * math.pi)

    def get_square(self):
        S_curcle = math.pi * self.radius ** 2  # площадь круга
        return S_curcle


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = (sum(self.__sides) / 2)
        side1 = self.__sides[0]
        side2 = self.__sides[1]
        side3 = self.__sides[2]
        s_triangle = (p * ((p - side1) * (p - side2) * (p - side3))) ** 0.5
        return s_triangle  # площадь треугольника


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides: int):
        super().__init__(color, *sides)
        self.sides = list(sides)
        if len(self.sides) == 1:
            new_list = [sides[0]] * self.sides_count
            self.set_sides(*new_list)
        if len(sides) == self.sides_count:
            self.set_sides = (sides)
        # else:
        #     self.set_sides(*([1]*self.sides_count))
        self.filled = True

    def get_volume(self):
        VCube = self.get_sides()[0] ** 3
        return VCube  # объем куба


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
