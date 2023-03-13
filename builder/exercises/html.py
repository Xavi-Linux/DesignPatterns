from abc import ABC, abstractmethod
from typing import List


#product class:
class HtmlElement:
    indent_size = 2

    def __init__(self, tag: str, content: str):
        self.tag = tag
        self.content = content
        self.children: List['HtmlElement'] = []
        self.parent = None

    def __recursive_str(self, indent) -> str:
        indent_text = ' ' * self.indent_size * indent
        if not self.children:

            return f'{indent_text}<{self.tag}>{self.content}</{self.tag}>'

        child_lines: List[str] = []
        for child in self.children:
            child_lines.append(
                f'{self.content}\n{child.__recursive_str(indent + 1)}'
            )

        return f'{indent_text}<{self.tag}>' + ''.join(child_lines) + '\n' f'{indent_text}<\{self.tag}>'

    def __str__(self):
        return self.__recursive_str(0)


#Abstract builder
class HtmlBuilder(ABC):

    def __init__(self, root: HtmlElement):
        self.root = root
        self.last_node = root

    @abstractmethod
    def add_child(self, tag: str, content: str) -> 'HtmlBuilder':
        return NotImplemented

    def __str__(self) -> str:
        return str(self.root)

    def get_parent(self) -> 'HtmlBuilder':
        if self.last_node.parent:
            self.last_node = self.last_node.parent

        return self

    def get_root(self) -> 'HtmlBuilder':
        self.last_node = self.root

        return self


#Implemented builder
class HtmlDocument(HtmlBuilder):

    def __init__(self, root=HtmlElement('html', '')):
        HtmlBuilder.__init__(self, root)

    def add_child(self, tag: str, content: str) -> HtmlBuilder:
        self.last_node.children.append(
            HtmlElement(tag, content)
        )
        self.last_node.children[-1].parent = self.last_node
        self.last_node = self.last_node.children[-1]

        return self


if __name__ == '__main__':

    # Single node:
    node: HtmlElement = HtmlElement('h1', 'Hello!')
    print(node)
    print('-------------')
    #Document
    potions: HtmlDocument = HtmlDocument()
    potions.add_child('h2', 'Nice potions')\
           .get_root()\
           .add_child('ul', '') \
           .add_child('li', 'felix felicis')\
           .get_parent()\
           .add_child('li', 'veritaserum')\
           .get_root()\
           .add_child('h2', 'Bad potions')

    print(potions)
