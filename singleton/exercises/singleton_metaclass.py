
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = type.__call__(cls, *args, **kwargs)

        return cls._instances[cls]


class TestClass(metaclass=Singleton):

    def __init__(self):
        print('new instance...')


if __name__ == '__main__':
    t1 = TestClass()
    t2 = TestClass()

    print(t1 is t2)
