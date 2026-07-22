class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

d = Duck()
d.fly()     # from Flyer
d.swim()    # from Swimmer
d.quack()   # from Duck
