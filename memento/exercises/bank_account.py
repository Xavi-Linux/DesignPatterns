from typing import Any


class Memento:

    def __init__(self, attributes: dict[str, Any]):
        self.__dict__ = attributes


class BankAccount:

    def __init__(self, balance: float = 0):
        self.balance = balance

    def deposit(self, amount: float) -> Memento:
        self.balance += amount

        return Memento(self.__dict__.copy())

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.__dict__.copy()


if __name__ == '__main__':

    ba = BankAccount()
    m1 = ba.deposit(50)
    m2 = ba.deposit(100)
    print(ba.balance)

    ba.restore(m1)
    print('Go back to memento 1:', ba.balance)

    ba.restore(m2)
    print('Go back to memento 2:', ba.balance)