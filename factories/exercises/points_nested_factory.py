from math import cos, sin


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    class _PointFactory:

        @staticmethod
        def new_cartesian_point(x,y):
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = _PointFactory()


if __name__ == '__main__':
    p1 = Point.factory.new_cartesian_point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p1, p2)
