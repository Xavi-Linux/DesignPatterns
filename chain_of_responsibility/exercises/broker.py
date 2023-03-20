from abc import ABC, abstractmethod
from enum import Enum


#Event class:
class Event(list):

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class QueryValues(Enum):
    ATTACK = 0
    DEFENSE = 1
    SPECIAL_ATTACK = 2
    SPECIAL_DEFENSE = 3
    SPEED = 4


class Query:

    def __init__(self, pokemon_name: str, query_value: QueryValues, default_value: int):
        self.value = default_value
        self.pokemon_name = pokemon_name
        self.query_value = query_value


class Broker:

    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        #Triggers call to the event handler.
        self.queries(sender, query)


class AbstractModifier(ABC):

    def __init__(self, broker: Broker, pokemon):
        #Both the modified and the modifier are given access to the Broker.
        self.broker = broker
        self.pokemon = pokemon
        #Enqueue the class' handler to the list of events
        self.broker.queries.append(self.handle)

    @abstractmethod
    def handle(self, sender, query):
        return NotImplemented

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #Dequeue the class' handler to the list of events
        self.broker.queries.remove(self.handle)


class IncreaseAttack(AbstractModifier):

    def handle(self, sender, query: Query):
        #Since the broker can be used by multiple pokemons instances, we use the pokemon's name to identify which one
        #the modifier is applied to. Additionally, since all modifiers are executed, we use the query value to identify
        #what event to perform at each modifier's call.
        if self.pokemon.name == sender.name and query.query_value == QueryValues.ATTACK:
            query.value += 1


class IncreaseDefense(AbstractModifier):

    def handle(self, sender, query):
        if self.pokemon.name == sender.name and query.query_value == QueryValues.DEFENSE:
            query.value += 1


class Pokemon:

    def __init__(
            self, broker: Broker, name:str, attack: int,
            defense: int, special_attack: int, special_defense: int, speed: int
    ):
        #store default values and create properties for current values
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense
        self.initial_special_attack = special_attack
        self.initial_special_defense = special_defense
        self.initial_speed = speed
        self.broker = broker

    @property
    def attack(self) -> int:
        query = Query(self.name, QueryValues.ATTACK, self.initial_attack)
        self.broker.perform_query(self, query)
        return query.value

    @property
    def defense(self) -> int:
        query = Query(self.name, QueryValues.DEFENSE, self.initial_defense)
        self.broker.perform_query(self, query)
        return query.value

    @property
    def special_attack(self) -> int:
        query = Query(self.name, QueryValues.SPECIAL_ATTACK, self.initial_special_attack)
        self.broker.perform_query(self, query)
        return query.value

    @property
    def special_defense(self) -> int:
        query = Query(self.name, QueryValues.SPECIAL_DEFENSE, self.initial_special_defense)
        self.broker.perform_query(self, query)
        return query.value

    @property
    def speed(self) -> int:
        query = Query(self.name, QueryValues.SPEED, self.initial_speed)
        self.broker.perform_query(self, query)
        return query.value

    def __str__(self) -> str:
        return f'{self.name}:\n- attack: {self.attack}\n- defense: {self.defense}\n' \
               f'- special attack: {self.special_attack}\n- special defense: {self.special_defense}\n' \
               f'- speed: {self.speed}'


if __name__ == '__main__':
    #The same broker instance can be used by multiple pokemons
    game = Broker()
    pikachu = Pokemon(game, 'pikachu', 10, 12, 15, 9, 15)
    print('Before:')
    print(pikachu)
    with IncreaseAttack(game, pikachu):
        print('While modifier is taking effect')
        print(pikachu)

    print('After:')
    print(pikachu)
    print('increase defense')
    with IncreaseDefense(game, pikachu):
        print(pikachu)
