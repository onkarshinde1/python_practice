class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} starting up...")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving!")


v = Car("Maruti")
v.drive()
v.start()
