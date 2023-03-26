"""
Intrusive = change every class to add similar functionality (eval, print)
"""


class FloatExpr:

    def __init__(self, value: float):
        self.value = value

    def print(self, buffer: list) -> None:
        buffer.append(str(self.value))

    def eval(self) -> float:
        return self.value


class AddOp:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer: list) -> None:
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self) -> float:
        return self.left.eval() + self.right.eval()


if __name__ == '__main__':
    expression = AddOp(
        left=FloatExpr(5),
        right=AddOp(FloatExpr(6), FloatExpr(7))
    )
    buffer = []
    expression.print(buffer)
    print(''.join(buffer))
    print(expression.eval())
