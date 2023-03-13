

class Person:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    def __init__(self):
        self.people_num = 0

    def create_person(self, name):
        p = Person(self.people_num, name)
        self.people_num += 1

        return p


if __name__ == '__main__':

    pf = PersonFactory()
    p1 = pf.create_person('Manolo')
    p2 = pf.create_person('Paquita')
