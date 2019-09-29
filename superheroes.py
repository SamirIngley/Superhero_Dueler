

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
        return random.randint(0, self.max_block)

class Weapon(Ability):
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        return random.randint((self.max_damage/2), (self.max_damage))


class Hero:
    def __init__(self, name, starting_health=200):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.weapons = list()
        self.current_health = starting_health
        self.starting_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def attack(self):
        for ability in self.abilities:
            #print(f' Ability: {ability.name}')
            return ability.attack()

        for weapon in self.weapons:
            return weapon.attack()

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        for armor in self.armors:
            print(f' Defense: {armor.name}')
            return armor.block()

    def take_damage(self, incoming_damage):
        self.current_health -= incoming_damage


    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():

            first_attack = self.attack()
            opponent_attack = opponent.attack()

            opponent.take_damage(first_attack)
            self.take_damage(opponent_attack)

        if self.is_alive() == False and opponent.is_alive() == False:
            print("Stalemate!")
        elif self.is_alive() == False:
            print(f"{opponent.name} won!")
        else:
            print(f"{self.name} won!")

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                print("He's not part of this team!")
            return self.heroes
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)










#
# if __name__ == "__main__":
#
    # SuperMan = Hero("SuperMan", 200)
    # print(f" Name: {SuperMan.name}")
    # print(f" Health: {SuperMan.current_health}")
    #
    # lazereyes = Ability("lazer 👁", 100)
    # SuperMan.add_ability(lazereyes)
    #
    # steelbody = Armor("steelbody  🦹🏾‍♂️", 100)
    # SuperMan.add_armor(steelbody)
    #
    # print(f' Defense Power: {SuperMan.defend()}')
    # print(f' Ability power : {SuperMan.attack()}')
    #
    # SuperMan.take_damage(59)
    # print(f' current health: {SuperMan.current_health}')
    #
    # SuperMan.take_damage(120)
    # print(SuperMan.is_alive())
    # SuperMan.take_damage(300)
    # print(SuperMan.is_alive())
    #
    # SuperMan.fight('yourmom')
    #
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    #
    # hero1.fight(hero2)
