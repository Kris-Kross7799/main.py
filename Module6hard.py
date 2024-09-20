class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides: list):
        self.__color=list(color)
        for i in sides:
            if len(sides) == self.sides_count:  # проверка длины списка sides и количества сторон фигуры
                self.__sides = sides
            else:
                self.__sides = [1] * self.sides_count
            self.filled = True

    def __is_valid_color(self, *colors):
        for i in colors:
            if len(colors) == 3 and 0 <= isinstance(i, int) <= 255:
                return True
        else:
            return False

    def set_color(self, r, g, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        for i in new_sides:
            if not isinstance(i, int) or i <= 0 or len(new_sides) != self.sides_count:
                return False
        return True

    def get_sides(self):
        return (self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [1] * self.sides_count
        self.radius = self.__sides[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.r ** 2)  # площадь круга


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        return (sum(self.__sides) / 2) * 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = [sides[0]] * self.sides_count
        self.Filled = True

    def get_volume(self):
        return self.__sides[0] ** 3  # площадь куба



# Проверка кода
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
