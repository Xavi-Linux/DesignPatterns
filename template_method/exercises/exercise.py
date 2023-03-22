from abc import ABC, abstractmethod


class Program(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    def run(self):
        self.start()
        self.end()


class EnglishProgram(Program):

    def start(self):
        print(f'Loading {self.name}...')
        print('running...')

    def end(self):
        print(f'Ending {self.name}...')


class CatalanProgram(Program):

    def start(self):
        print(f'Iniciant {self.name}...')
        print('executant...')

    def end(self):
        print(f'Tancant {self.name}...')


if __name__ == '__main__':
     e = EnglishProgram('Peggy')
     c = CatalanProgram('Pegaso')

     e.run()
     c.run()