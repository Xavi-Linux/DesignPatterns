

class Pokemon:

    def __init__(self, name:str, attack: int, defense: int, special_attack: int, special_defense: int, speed: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def __str__(self) -> str:
        return f'{self.name}:\n- attack: {self.attack}\n- defense: {self.defense}\n' \
               f'- special attack: {self.special_attack}\n- special defense: {self.special_defense}\n' \
               f'- speed: {self.speed}'


class PokemonModifier:

    def __init__(self, pokemon: Pokemon):
        self.pokemon = pokemon
        self.next_modifier = None

    def add_modifier(self, modifier: 'PokemonModifier') -> None:
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)

        else:
            self.next_modifier = modifier

    def handle(self, *args, **kwargs):
        if self.next_modifier:
            self.next_modifier.handle()


class IncreaseAttack(PokemonModifier):

    def handle(self):
        self.pokemon.attack += 1
        #call to the Parent class to generate the chain
        #do not call if you want to break the chain
        PokemonModifier.handle(self)


if __name__ == '__main__':

    pikachu = Pokemon('pikachu', 10, 12, 15, 9, 15)
    print(pikachu)
    pikamodifier = PokemonModifier(pikachu)

    pikamodifier.add_modifier(IncreaseAttack(pikachu))
    pikamodifier.add_modifier(IncreaseAttack(pikachu))
    pikamodifier.handle()
    print(pikachu)
