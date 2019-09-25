
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, name):
        print(f"{name} is eating")
        return

    def drink(self, name):
        print(f"{name} is drinking")
        return


class Dog(Animal):
    def __init__(self, name):
        
