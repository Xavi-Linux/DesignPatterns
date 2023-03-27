from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def on(self, switch) -> None:
        return NotImplemented

    @abstractmethod
    def off(self, switch) -> None:
        return NotImplemented


class OnState(State):

    def __init__(self):
        print('Light is on')

    def on(self, switch) -> None:
        print('Light is already on!')

    def off(self, switch) -> None:
        switch.state = OffState()


class OffState(State):

    def __init__(self):
        print('Light is off')

    def on(self, switch) -> None:
        switch.state = OnState()

    def off(self, switch) -> None:
        print('Light is already off')


class Switch:

    def __init__(self):
        self.state = OffState()

    def on(self) -> None:
        print('Turning the light on...')
        self.state.on(self)

    def off(self) -> None:
        print('Turning the light off...')
        self.state.off(self)


if __name__ == '__main__':

    sw = Switch()

    sw.on()
    sw.off()
    sw.on()
    sw.on()
    sw.off()
    sw.off()
