

class User:
    """
    Flyweight implementation
    """
    names = []

    def __init__(self, name: str):
        def retrieve_index(string: str) -> int:
            if string in User.names:
                return User.names.index(string)

            else:
                User.names.append(string)
                return len(User.names) - 1

        self.name = [retrieve_index(v) for v in name.split(' ')]

    def __str__(self) -> str:
        return ' '.join([User.names[i] for i in self.name])


if __name__ == '__main__':

    u1 = User('Charmander Pérez')
    u2 = User('Squirtle Gómez')
    u3 = User('Bulbasur Pérez')

    print('user1:')
    print(u1.name)
    print(u1)

    print('user2:')
    print(u2.name)
    print(u2)

    print('user3:')
    print(u3.name)
    print(u3)

    print(User.names)

    u4 = User('Charmander Gómez')
    print(u4.name)
    print(u4)

    print(User.names)