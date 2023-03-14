from abc import ABC, abstractmethod


class Renderer(ABC):

    @property
    @abstractmethod
    def what_to_render_as(self) -> str:
        return NotImplemented


class VectorRenderer:

    @property
    def what_to_render_as(self) -> str:
        return 'lines'


class RasterRenderer:

    @property
    def what_to_render_as(self) -> str:
        return 'pixels'


class Shape(ABC):

    def __init__(self, renderer: Renderer):
        self.renderer = renderer
        self.name = None

    def __str__(self) -> str:
        return f'Drawing {self.name} as {self.renderer.what_to_render_as}'


class Triangle(Shape):

    def __init__(self, renderer: Renderer):
        Shape.__init__(self, renderer)
        self.name = 'triangle'


class Square(Shape):

    def __init__(self, renderer: Renderer):
        Shape.__init__(self, renderer)
        self.name = 'square'


if __name__ == '__main__':

    v_renderer = VectorRenderer()
    r_renderer = RasterRenderer()

    tv, tr = Triangle(v_renderer), Triangle(r_renderer)

    print(tv)
    print(tr)