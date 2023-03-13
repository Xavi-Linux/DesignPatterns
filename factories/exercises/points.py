from math import cos, sin


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @classmethod
    def new_cartesian_point(cls, x,y):
        return cls(x, y)

    @classmethod
    def new_polar_point(cls, rho, theta):
        return cls(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = Point.new_cartesian_point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p1, p2)
