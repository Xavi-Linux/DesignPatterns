from collections.abc import Iterable, Iterator
from typing import Union, Literal


class InOrder:

    def __init__(self, node: 'Node'):
        self.node = node

    def __call__(self):
        def traverse(current: 'Node') -> 'Node':
            if current.left:
                for left in traverse(current.left):
                    yield left

            yield current
            if current.right:
                for right in traverse(current.right):
                    yield right

        for node in traverse(self.node):
            yield node


class PreOrder(InOrder):

    def __call__(self):
        def traverse(current: 'Node') -> 'Node':
            yield current
            if current.left:
                for left in traverse(current.left):
                    yield left

            if current.right:
                for right in traverse(current.right):
                    yield right

        for node in traverse(self.node):
            yield node


class PostOrder(InOrder):

    def __call__(self):
        def traverse(current: 'Node') -> 'Node':
            if current.left:
                for left in traverse(current.left):
                    yield left

            if current.right:
                for right in traverse(current.right):
                    yield right

            yield current

        for node in traverse(self.node):
            yield node


class Node(Iterable):

    def __init__(self, value: int, left: Union['Node', None] = None, right: Union['Node', None] = None):
        self.value= value
        self.parent: Union['Node', None] = None
        self.left = left
        self.right = right
        if left:
            self.left.parent = self

        if right:
            self.right.parent = self

        self._strategy = 'inorder'

    def set_strategy(self, strategy: Literal['inorder', 'preorder', 'postorder']) -> None:
        self._strategy = strategy

    def __iter__(self) -> Iterator:
        if self._strategy == 'inorder':
            return InOrder(self)()
        elif self._strategy == 'preorder':
            return PreOrder(self)()
        elif self._strategy == 'postorder':
            return PostOrder(self)()

    def __str__(self) -> str:
        return f'{self.value}'


if __name__ == '__main__':

    a = Node(1, Node(2), Node(3))
    a.left.left = Node(4)
    a.left.right = Node(5)
    for node in a:
        print(node)

    print('-----')
    a.set_strategy('preorder')
    for node in a:
        print(node)

    print('-------')
    a.set_strategy('postorder')
    for node in a:
        print(node)