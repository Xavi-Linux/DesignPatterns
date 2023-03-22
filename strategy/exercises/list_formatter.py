from abc import ABC
from typing import Literal

class Strategy(ABC):

    @staticmethod
    def start(buffer: list) -> None:
        pass

    @staticmethod
    def end(buffer: list) -> None:
        pass

    @staticmethod
    def append(buffer: list, item: str) -> None:
        pass


class HTML(Strategy):

    @staticmethod
    def start(buffer: list) -> None:
        buffer.append('<ul>\n')

    @staticmethod
    def end(buffer: list) -> None:
        buffer.append('</ul>')

    @staticmethod
    def append(buffer: list, item) -> None:
        buffer.append(f'<li>{item}</li>\n')


class MarkDown(Strategy):

    @staticmethod
    def append(buffer: list, item: str) -> None:
        buffer.append(f'* {item}\n')


class ListFormatter:

    def __init__(self, strategy=HTML()):
        self.strategy = strategy
        self._buffer = []

    def append_elements(self, elements: list[str]) -> None:
        if not self._buffer:
            self.strategy.start(self._buffer)

        for element in elements:
            self.strategy.append(self._buffer, element)

        self.strategy.end(self._buffer)

    def __str__(self) -> str:
        return ''.join(self._buffer)

    def clear(self) -> None:
        self._buffer = []

    def set_formatter(self, formatter: Literal['html', 'markdown']) -> None:
        if formatter == 'html':
            self.strategy = HTML()
        elif formatter == 'markdown':
            self.strategy = MarkDown()

        self._buffer.clear()


if __name__ == '__main__':
    pokemon: list[str] = [
        'pikachu',
        'charmander',
        'squirtle',
        'bulbasur'
    ]

    processor = ListFormatter()

    processor.append_elements(pokemon)

    print(processor)

    processor.set_formatter('markdown')

    processor.append_elements(pokemon)
    print(processor)
