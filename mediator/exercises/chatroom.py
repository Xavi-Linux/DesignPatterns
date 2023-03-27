

class Person:

    def __init__(self, name: str):
        self.name = name
        self.message_log: list[str] = list()
        self.room = None

    def receive(self, source: str, message: str) -> None:
        s: str = f'Message from {source}: {message}'
        print(s)
        self.message_log.append(s)

    def write_to_room(self, message: str) -> None:
        self.room.broadcast(self, message)

    def send_private_message(self, person: str, message: str) -> None:
        self.room.pass_message(self, person, message)

    def log_out(self) -> None:
        self.room.leave(self)


class ChatRoom:

    def __init__(self, topic: str):
        self.topic = topic
        self.people: list[Person] = list()

    def broadcast(self, source: Person, message: str) -> None:
        for person in self.people:
            if person.name != source.name:
                person.receive('Room ' + self.topic, message)

    def join(self, person: Person) -> None:
        person.room = self
        self.people.append(person)
        self.broadcast(person, f'{person.name} has just joined the room')

    def leave(self, person: Person) -> None:
        self.people.remove(person)
        self.broadcast(person, f'{person.name} has just left the room')

    def pass_message(self, source: Person, dest: str, message: str) -> None:
        for person in self.people:
            person: Person
            if person.name == dest:
                person.receive(source.name, message)
                break


if __name__ == '__main__':

    room = ChatRoom('Food')

    p1 = Person('James')
    p2 = Person('Judy')

    room.join(p1)
    room.join(p2)
    p2.write_to_room('Hey all! Just hanging around...')
    p1.send_private_message('Judy', 'It seems it is the two of us here...')

    p3 = Person('Richard')
    room.join(p3)
    p3.write_to_room('How are you doing?')

    p1.write_to_room('Richard, the room is not large enough for the two of us')
    room.leave(p1)