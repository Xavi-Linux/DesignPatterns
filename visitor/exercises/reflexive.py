from abc import ABC


class Expr(ABC):
    pass


class FloatExpr(Expr):

    def __init__(self, value: float):
        self.value = value

    def eval(self) -> float:
        return self.value


class AddOp(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self) -> float:
        return self.left.eval() + self.right.eval()


class Printer:

    @staticmethod
    def print(expr: Expr, buffer: list) -> None:
        if isinstance(expr, FloatExpr):
            buffer.append(str(expr.value))

        elif isinstance(expr, AddOp):
            buffer.append('(')
            Printer.print(expr.left, buffer)
            buffer.append('+')
            Printer.print(expr.right, buffer)
            buffer.append(')')


Expr.print = lambda a, b,: Printer.print(a, b)


class Evaluator:

    @staticmethod
    def eval(expr: Expr) -> float:
        result = 0
        if isinstance(expr, FloatExpr):
            result += expr.value

        else:
            result += Evaluator.eval(expr.left) + Evaluator.eval(expr.right)

        return result


Expr.eval = lambda e: Evaluator.eval(e)


if __name__ == '__main__':
    expression = AddOp(
        left=FloatExpr(5),
        right=AddOp(FloatExpr(6), FloatExpr(7))
    )
    buffer = []
    expression.print(buffer)
    print(''.join(buffer))
    print(expression.eval())

