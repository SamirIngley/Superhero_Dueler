

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
        damage = int(incoming_damage)
        self.current_health -= damage

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
            # headsortails = random.choice(0,1)
            # if headsortails == 0

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
        self.num_heroes = 0

    def add_hero(self, hero):
        self.heroes.append(hero)
        self.num_heroes += 1

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
        fighting = True
        team_one = []
        team_two = []

        while fighting:
            team_one.clear()
            team_two.clear()
            for hero in self.heroes:
                print("self hero", hero)
                # if hero.is_alive():
                #     team_one.append(hero)
            for hero in other_team.heroes:
                print("other hero", hero)
                # if hero.is_alive():
                #     team_two.append(hero)
            if len(team_one) <= 0 or len(team_two) <= 0:
                fighting = False
            else:
                hero_one = choice(team_one)
                hero_two = choice(team_two)
                hero_one.fight(hero_two)

        # your_hero = self.heroes[random.randint(0, (len (self.heroes))-1)]
        # opponent_hero = self.heroes[random.randint(0, (len(other_team.heroes))-1)]
        # your_hero.fight(opponent_hero)

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
        self.team_one: []
        self.team_two: []

    def create_ability(self):
        name = input("What's the ability's name? ")
        max_damage = int(input("Max Damage? "))
        ability = Ability(name, max_damage)
        return ability

    def create_weapon(self):
        name = input("What's the weapon's name? ")
        max_damage = int(input("Max Damage "))
        weapon = Weapon(name, max_damage)
        return weapon

    def create_armor(self):
        name = input("What's the armor name? ")
        max_block = int(input("Max Defense? "))
        armor = Armor(name, max_block)
        return armor

    def create_hero(self):
        name = input("Hero name? ")
        new_Hero = Hero(name, starting_health = 200)

        ability = input("Add abilities? Y/N ")
        if ability.lower() == "y":
            new_Hero.add_ability(self.create_ability())

        weapon = input("Add weapons? Y/N ")
        if weapon.lower() == "y":
            new_Hero.add_weapon(self.create_weapon())

        armor = input("Add armor? Y/N")
        if armor.lower() == "y":
            new_Hero.add_armor(self.create_armor())

    def build_team_one(self):
        team_name = input("Team 1 Name: ")
        self.team_one = Team(team_name)
        num_heroes = int(input("How many heroes on team 1? "))
        for amount in range (num_heroes):
            Hero = self.create_hero()
            print(Hero)
            self.team_one.append(Hero)

    def build_team_two(self):
        team_name = input("Team 2 Name: ")
        self.team_two = Team(team_name)
        num_heroes = int(input("How many heroes on team 2? "))
        for amount in range (num_heroes):
            Hero = self.create_hero()
            print(Hero)
            self.team_two.append(Hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print('Team One stats:')
        print(self.team_one.stats)
        print('Team Two stats:')
        print(self.team_two.stats)

        if (self.team_one.stats > self.team_two.stats):
            print(f'{self.team_one} won!')
        elif (self.team_one.stats < self.team_two.stats):
            print(f'{self.team_two} won!')
        else:
            print('Draw Match!')

        team_one_raw_kdr = 0
        team_one_alive_count = 0
        team_one_alive_names = list()
        for hero in self.team_one.heroes:
            raw_kdr += self.team_one.stats
            if hero.isalive():
                team_one_alive += 1
                team_one_alive_names.append(hero.name)

        team_two_raw_kdr = 0
        team_two_alive_count = 0
        team_two_alive_names = list()
        for hero in self.team_two.heroes:
            raw_kdr += self.team_one.stats
            if hero.isalive():
                team_two_alive += 1
                team_two_alive_names.append(hero.name)

        team_one_overall_kd = team_one.stats / team_one.num_heroes
        team_two_overall_kd = team_two.stats / team_two.num_heroes

        print('Team One Survivors:')
        for name in team_one_alive_names:
            print(name)

        print('Team Two Survivors')
        for name in team_two_alive_names:
            print(name)




#
#
#
# if __name__ == "__main__":
#     arena = Arena()
#     arena.build_team_one()
#     arena.build_team_two()
#     arena.team_battle()
#     arena.show_stats()


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()



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
