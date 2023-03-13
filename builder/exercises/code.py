
class Attribute:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'self.{self.name} = {self.value}'


class Class:

    def __init__(self, name):
        self.name = name
        self.attributes = []

    def add_attribute(self, name, value):
        self.attributes.append(Attribute(name, value))

    def __str__(self):
        class_line = f'class {self.name}:\n'
        init_line = f'  def __init__(self):\n'
        attr_lines = []
        for attr in self.attributes:
            attr_lines.append(' ' * 4 + str(attr) + '\n')

        return class_line + init_line + ''.join(attr_lines)


class CodeBuilder:
    def __init__(self, root_name):
        self._class = Class(root_name)

    def add_field(self, type, name):
        self._class.add_attribute(type, name)

        return self

    def __str__(self):
        return str(self._class)


if __name__ == '__main__':
    c = CodeBuilder('Person').add_field('name', '"Manolo"').add_field('age', 31)

    print(c)