

class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square of side {self.side}'


class ColoredShape(Shape):

    def __init__(self, shape: Shape, color):
        self.color = color
        self.shape = shape

    def __str__(self):
        return f'{self.shape} has the color {self.color}'

    def __getattr__(self, item):
        return getattr(self.shape, item)


if __name__ == '__main__':

    c = Circle(5)
    s = Square(2)
    cs = ColoredShape(c, 'red')
    cs.resize(2)
    print(cs)
    ss = ColoredShape(s, 'blue')
    ss.resize(2)
    print(s)
