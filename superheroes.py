

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
        self.current_health = starting_health
        self.starting_health = starting_health
        self.deaths = 0
        self.kills = 0


    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):

        for ability in self.abilities:
            #print(f' Ability: {ability.name}')
            return ability.attack()


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

    #Tracking statistics
    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths


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
            add_deaths(1)
        else:
            print(f"{self.name} won!")
            add_kill(1)

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
                return
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        your_hero = random.choice(self.heroes)
        opponent_hero = random.choice(other_team)
        your_hero.fight(opponent)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        # total_kills = 0
        # total_deaths = 0
        # kdr = 0
        # for hero in self.heroes:
        #     hero.add_kills(hero.kills)
        #     total_deaths += hero.num_deaths
        total_kills = 0
        total_deaths = 0
        kdr = 0
        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths
        if total_deaths == 0:
            kdr = total_deaths
        else:
            kdr = total_kills/total_deaths
        return kdr






class Arena:
    def __init__(self):
        team_one: None
        team_two: None

    def create_ability(self):
        name = input("What's the ability's name?")
        max_damage = int(input("Max Damage?"))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = ("What's the weapon's name?")
        max_damage = int(input("Max Damage"))
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What's the armor name")
        max_block = input("Max Defense?")
        return Armor(name, max_block)

    def create_hero(self):
        name = input("Hero name?")
        new_Hero = Hero(name, starting_health = 200)
        while (input("Add abilities? Y/N")) == ("Y" or "y"):
            new_Hero.add_ability(self.create_ability())
            print(f"Added {ability_name}")
        while (input("Add weapons? Y/N")) == ("Y" or "y"):
            new_Hero.add_weapon(self.create_weapon())
            print(f"Added {weapon_name}")
        while (input("Add armor? Y/N")) == ("Y" or "y"):
            new_Hero.add_armor(self.create_armor())
            print(f"Added {armor_name}")










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
