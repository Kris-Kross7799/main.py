class Horse:
    def __init__(self, x_distance=0, sound="Frr"):
        self.x_distance = x_distance
        self.sound = sound
        # super().fly()

    def run(self, dx):
        self.dx = dx
        self.x_distance +=dx
        return self.x_distance


class Eagle:
    def __init__(self, y_distance=0, sound="I train, eat,sleep and repeat"):
        self.sound = sound
        self.y_distance = y_distance

    def fly(self, dy):
        self.dy = dy
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        tuple = (self.x_distance, self.y_distance)
        return tuple

    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()


