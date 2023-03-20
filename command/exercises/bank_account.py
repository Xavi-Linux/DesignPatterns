from abc import ABC, abstractmethod
from typing import Literal


class BankAccount:

    OVERDRAFT_LIMIT: float = 0

    def __init__(self, balance: float = 0):
        self.balance = balance

    def deposit(self, amount: float) -> bool:
        print(f'Adding: €{amount}')
        self.balance += amount

        return True

    def withdraw(self, amount:float) -> bool:
        remainder = self.balance - amount
        if remainder > self.OVERDRAFT_LIMIT:
            print(f'Withdrawing: €{amount}')
            self.balance = remainder

            return True

        return False


class Command(ABC):

    def __init__(self, *args, **kwargs):
        self.success = False

    @abstractmethod
    def invoke(self):
        return NotImplemented

    @abstractmethod
    def undo(self):
        return NotImplemented


class BankAccountCommand(Command):

    def __init__(self, bank_account: BankAccount, command: Literal['deposit', 'withdraw'], amount: float):
        Command.__init__(self)
        self.bank_account = bank_account
        self.command = command
        self.amount = amount

    def invoke(self):
        print(f'balance before execution: {self.bank_account.balance}')
        if self.command == 'deposit':
            self.success = self.bank_account.deposit(self.amount)

        elif self.command == 'withdraw':
            self.success = self.bank_account.withdraw(self.amount)

        print(f'balance after execution: {self.bank_account.balance}')

    def undo(self):
        print(f'balance before execution: {self.bank_account.balance}')
        if self.command=='deposit' and self.success:
            self.bank_account.withdraw(self.amount)

        elif self.command=='withdraw' and self.success:
            self.bank_account.deposit(self.amount)
        print(f'balance after execution: {self.bank_account.balance}')


class CompositeCommand(Command, list):

    def __init__(self, commands: list[Command]):
        list.__init__(self)
        self.extend(commands)

    def invoke(self):
        for command in self:
            command: Command
            command.invoke()
            if not command.success:
                break

    def undo(self):
        for command in reversed(self):
            command: Command
            if command.success:
                command.undo()


class TransferCommand(CompositeCommand):

    def __init__(self, from_acc: BankAccount, to_acc: BankAccount, amount: float):
        CompositeCommand.__init__(self,
                                  commands=[
                                        BankAccountCommand(from_acc, 'withdraw', amount),
                                        BankAccountCommand(to_acc, 'deposit', amount)
                                  ]
        )


if __name__ == '__main__':
    bank_account = BankAccount(100)
    recipient = BankAccount()
    transfer = TransferCommand(bank_account, recipient, 10)
    transfer.invoke()
    transfer.undo()
