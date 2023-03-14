

class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:

    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


if __name__ == '__main__':

    s = Square(10)
    adapter = SquareToRectangleAdapter(s)
    print(calculate_area(adapter)) #10
    s.side = 14
    print(calculate_area(adapter)) #14
