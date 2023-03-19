

class Driver:

    def __init__(self, name: str, age: int):
        self.name= name
        self.age = age

    def __str__(self) -> str:
        return f'Driver with name {self.name} and age {self.age}'


class Car:

    def __init__(self, driver: Driver):
        self.driver = driver
        self.on = False

    def drive(self) -> None:
        print('starting engine')
        self.on = True
        print(f'{self.driver} is driving')

    def __str__(self) -> str:
        return f'Car driven by {self.driver}'


class RestrictedCar:
    """
    Underage people may not drive
    """

    def __init__(self, driver: Driver):
        self.driver = driver
        self._car = Car(driver)

    def __getattr__(self, item):
        if item == 'drive' and self.driver.age < 18:
            raise Exception('Driver is underage')

        else:
            return getattr(self._car, item)


if __name__ == '__main__':

    underage = Driver('James', 17)
    driver = Driver('Ollie', 20)

    c1 = RestrictedCar(underage)
    c2 = RestrictedCar(driver)

    c2.drive()
    c1.drive()
