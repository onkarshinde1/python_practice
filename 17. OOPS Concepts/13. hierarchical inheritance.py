class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

class Cow(Animal):
    def moo(self):
        print("Mooo!")

d = Dog("Rex")
c = Cat("Whiskers")
cow = Cow("Bessie")

# All inherit breathe() from Animal
d.breathe()
c.breathe()
cow.breathe()
