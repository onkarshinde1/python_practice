class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):
    def feed_young(self):
        print("Feeding young...")

class Dog(Mammal):
    def bark(self):
        print("Woof!")

d = Dog()
d.breathe()      # from Animal (grandparent)
d.feed_young()   # from Mammal (parent)
d.bark()         # from Dog itself
