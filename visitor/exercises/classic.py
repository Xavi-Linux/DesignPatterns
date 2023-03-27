from abc import ABC
from typing import Callable, Union


class Expr(ABC):

    def accept(self, visitor) -> None:
        visitor.visit(self)


class FloatExpr(Expr):

    def __init__(self, value: float):
        self.value = value


class AddOp(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right


#Store functions having the same name
_funcs = {}


def visitor(type_: Union[FloatExpr, AddOp]):
    def declaration(func: Callable):
        _funcs[func.__qualname__ + '_' + type_.__name__] = func

        def instantiation(*args, **kwargs):
            return _funcs[func.__qualname__ + '_' + type(args[1]).__name__](*args, **kwargs)

        return instantiation

    return declaration


class ExprPrinter:

    def __init__(self):
        self.buffer = []

    @visitor(FloatExpr)
    def visit(self, expr: FloatExpr):
        self.buffer.append(str(expr.value))

    @visitor(AddOp)
    def visit(self, expr: AddOp):
        self.buffer.append('(')
        expr.left.accept(self)
        self.buffer.append('+')
        expr.right.accept(self)
        self.buffer.append(')')

    def __str__(self) -> str:
        return ''.join(self.buffer)


if __name__ == '__main__':
    expression = AddOp(
        left=FloatExpr(5),
        right=AddOp(FloatExpr(6), FloatExpr(7))
    )

    printer = ExprPrinter()

    printer.visit(expression)
    print(printer)