from math import pow


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}'


class Line:

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f'---Line---\nstart at: {str(self.start)}\nend at: {str(self.end)}'


class Rectangle(list):

    def __init__(self, bottom_left_point: Point, width: int, height: int):
        list.__init__(self)
        self.xy: Point = bottom_left_point
        self.width: int = width
        self.height: int = height
        self.extend(
            [
                Line(self.xy, Point(self.xy.x + self.width, self.xy.y)),
                Line(self.xy, Point(self.xy.x, self.xy.y + self.height)),
                Line(Point(self.xy.x, self.xy.y + self.height), Point(self.xy.x + self.width, self.xy.y + self.height)),
                Line(Point(self.xy.x + self.width, self.xy.y), Point(self.xy.x + self.width, self.xy.y + self.height))
            ]
        )


class LineToPointAdapter(list):
    """
    It converts a line into a list of points
    """

    def __init__(self, line: Line):
        list.__init__(self)
        self.line: Line = line

        num_points = pow(
            (self.line.end.x - self.line.start.x) ** 2 + (self.line.end.y - self.line.start.y) ** 2,
            0.5
        )
        self.append(self.line.start)
        for p in range(0, int(num_points)):
            self.append(
                Point(1, 1) #TODO: tweak by including correct points
            )


#api to draw a point
def render_point(p: Point) -> None:
    print('.', end='')


if __name__=='__main__':
    rec = Rectangle(Point(1,1), 10, 10)
    for line in rec:
        adapter = LineToPointAdapter(line)
        print(f'\nPoints for {line}')
        for point in adapter:
            render_point(point)



