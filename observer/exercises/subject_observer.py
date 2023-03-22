from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Subject(ABC):

    def __init__(self, *args, **kwargs):
        self._observers: list[Observer] = list()

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer:Observer) -> None:
        self._observers.remove(observer)

    def notify_observer(self, *args, **kwargs) -> None:
        for observer in self._observers:
            observer.update(*args, **kwargs)


class Child(Subject):

    def __init__(self, name: str):
        Subject.__init__(self)
        self.name = name

    def behave_correctly(self) -> None:
        print('Behaving correctly')
        self.notify_observer(self.behave_correctly)

    def be_mischeavous(self):
        print('Mischiefs here and there')
        self.notify_observer(self.be_mischeavous)


class Parent(Observer):

    def __init__(self, name: str, child: Child):
        self.child = child
        self.name = name

    def update(self, method):
        if method == self.child.be_mischeavous:
            print(f'Hey {self.name}! Your child {self.child.name} is not behaving correctly')


if __name__ == '__main__':

    child = Child('Dave')
    father = Parent('David', child)
    child.be_mischeavous()

    child.register_observer(father)

    child.behave_correctly()
    child.behave_correctly()
    child.be_mischeavous()

    mother = Parent('Kate', child)
    child.register_observer(mother)
    child.behave_correctly()
    child.be_mischeavous()

    child.remove_observer(father)
    child.be_mischeavous()