"""
Question:
You are given a game scenario with classes Goblin and GoblinKing. Please implement the following rules:

    A goblin has base 1 attack/1 defense (1/1), a goblin king is 3/3.

    When the Goblin King is in play, every other goblin gets +1 Attack.

    Goblins get +1 to Defense for every other Goblin in play (a GoblinKing is a Goblin!).

Example:

    Suppose you have 3 ordinary goblins in play. Each one is a 1/3 (1/1 + 0/2 defense bonus).

    A goblin king comes into play. Now every goblin is a 2/4 (1/1 + 0/3 defense bonus from each other
    + 1/0 from goblin king)

The state of all the goblins has to be consistent as goblins are added and removed from the game.
"""
from abc import ABC, abstractmethod
from enum import Enum


class Event(list):

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Features(Enum):
    ATTACK = 0
    DEFENSE = 1


class Query:

    def __init__(self, instance, feature, default_value):
        self.instance = instance
        self.value = default_value
        self.feature = feature


class Game:

    def __init__(self):
        self.creatures = Event()

    def perform_query(self, sender, query):
        self.creatures(sender, query)


class AbstractModifier(ABC):

    def __init__(self, broker, *args, **kwargs):
        self.broker = broker
        self.broker.creatures.append(self.handle)

    @abstractmethod
    def handle(self, sender, query):
        return NotImplemented


class IncreaseAttack(AbstractModifier):

    def __init__(self, broker, value: int = 1):
        AbstractModifier.__init__(self, broker)
        self.value = value

    def handle(self, sender, query: Query):
        if not isinstance(sender, GoblinKing) and query.feature == Features.ATTACK:
            query.value += self.value


class IncreaseDefense(IncreaseAttack):

    def handle(self, sender, query: Query):
        if not isinstance(sender, GoblinKing) and query.feature == Features.DEFENSE:
            query.value += self.value


class Creature:

    instances = 0

    def __init__(self, game, attack, defense):
        self.initial_attack = attack
        self.initial_defense = defense
        self.game = game
        if Creature.instances > 0:
            IncreaseDefense(self.game)

        Creature.instances += 1

    @property
    def attack(self):
        query = Query(self, Features.ATTACK, self.initial_attack)
        self.game.perform_query(self, query)
        return query.value

    @property
    def defense(self):
        query = Query(self, Features.DEFENSE, self.initial_attack)
        self.game.perform_query(self, query)
        return query.value


class Goblin(Creature):

    def __init__(self, game, attack=1, defense=1):
        Creature.__init__(self, game, attack, defense)


class GoblinKing(Goblin):

    def __init__(self, game):
        Creature.__init__(self, game, 3, 3)
        IncreaseAttack(self.game)


if __name__ == '__main__':
    game = Game()
    g1 = Goblin(game)
    g2 = Goblin(game)
    g3 = Goblin(game)

    print(g2.defense, g2.attack)

    kg = GoblinKing(game)
    print(g1.defense, g1.attack)
    print(kg.defense, kg.attack)
