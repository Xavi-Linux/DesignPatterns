from copy import deepcopy


class Address:

    def __init__(self, city: str, street: str, desk: int):
        self.city = city
        self.street = street
        self.desk = desk

    def __str__(self) -> str:
        return f'{self.city}, {self.street}, desk {self.desk}'


class Employee:

    def __init__(self, name: str, address:Address):
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} {str(self.address)}'


class EmployeeFactory:

    def __init__(self):
        self._offices = {}

    def register_office(self, office_id: str, address: Address) -> None:
        self._offices[office_id] = address

    def get_registered_offices(self) -> str:
        return str(self._offices)

    def remove_office(self, office_id) -> None:
        del self._offices[office_id]

    def create_new_employee(self, name:str, office_id: str, desk: int) -> Employee:
        address: Address = deepcopy(self._offices[office_id])
        address.desk = desk

        return Employee(name, address)


if __name__ == '__main__':

    ef: EmployeeFactory = EmployeeFactory()
    offices = {
        'Barcelona': Address('Barcelona', 'Av. Diago 123 2 1', 0),
        'London': Address('London', '63 Picadilly', 0),
        'Miami': Address('Miami', '11 Horatio Avenue', 0)
    }
    for office in offices:
        ef.register_office(office, offices[office])

    employee1 = ef.create_new_employee('John Bull', 'London', 44)
    employee2 = ef.create_new_employee('Cisquet', 'Barcelona', 5)
    employee3 = ef.create_new_employee('Joaneta', 'Barcelona', 6)

    print(employee1)
    print(employee2)
    print(employee3)