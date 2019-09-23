

import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, max_block)

class Hero:
    def __init__(self, name, abilities, armors, current_health, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''
        self.name = name
        self.abilities = abilities
        self.armors = armors
        self.current_health = current_health
        self.starting_health = starting_health

    def add_ability(self, ability):
        abilities.append(ability)
        

    def attack():
        pass

    def defend(incoming_damage):
        pass

    def take_damage(damage):
        pass

    def is_alive():
        pass

    def fight(HeroClass):
        pass


if __name__ == "__main__":

    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
