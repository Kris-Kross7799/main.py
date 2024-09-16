class Figure:
    sides_count = 3

    def __init__(self, color: [], *sides: []):
        self.__color = color
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [sides[0]] * self.sides_count
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return r, g, b

    def set_color(self, r, g, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [self.r, self.g, self.b]
            return self.__color

    def is_valid_sizes(self, *new_sides):
        for i in new_sides:
            if isinstance(i, int) and i > 0 and len(new_sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return (self.__sides)

    def __len__(self):
            return sum(self.__sides)

    def set_sides(self, *new_sides):
            if self.is_valid_sizes(*new_sides):
                self.__sides = list(new_sides)


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
        return 3.14 * (self.r ** 2)              #площадь круга


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

    def get_volume(self):
        return self.__sides[0] ** 3

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

