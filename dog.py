



class Dog:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("<> sits")

    def roll(self):
        print("<> rolls")



my_dog = Dog("Rex", "SuperDog")

Dog.greeting = "Woah"
