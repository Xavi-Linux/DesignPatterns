

def singleton(_class):
    instances = {}

    def generate_instance(*args, **kwargs):
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)

        return instances[_class]

    return generate_instance


@singleton
class TestClass:

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':

    s1 = TestClass(1)
    s2 = TestClass(2)

    print(s1 is s2) #True
    print(s1.value)
    print(s2.value)
