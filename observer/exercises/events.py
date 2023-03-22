from typing import Callable


class Event(list):

    def __call__(self, *args, **kwargs):
        for func in self:
            func(*args, **kwargs)


class DefaultActions:

    @staticmethod
    def call_ft(name: str) -> None:
        print(f'Hello FT! This is {name} and I have just gone bankrupt')

    @staticmethod
    def sell_shares(name: str) -> None:
        print(f'Sell {name} shares before going bankrupt')

    @staticmethod
    def ask_for_bailout(name: str) -> None:
        print(f'This is {name}. May you bail me out?')


class Company:

    def __init__(self, name: str, budget: int):
        self.name = name
        self.budget = budget
        self.goes_bankrupt = Event()

    def invest(self, amount: int) -> None:
        self.budget -= amount
        if self.budget < 0:
            self.goes_bankrupt(self.name)

    def save_actions(self, action: Callable) -> None:
        self.goes_bankrupt.append(action)


if __name__ == '__main__':

    svb = Company('SVB', 100)
    svb.save_actions(DefaultActions.sell_shares)
    svb.save_actions(DefaultActions.call_ft)
    svb.save_actions(DefaultActions.ask_for_bailout)

    svb.invest(10)
    print('All good! Waiting for a return')
    svb.invest(85)
    print('All good! Waiting for a return')
    svb.invest(100)