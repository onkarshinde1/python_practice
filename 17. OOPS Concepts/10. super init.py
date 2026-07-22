class Vehicle:
    def __init__(self, brand: str) -> None:
        print("This is vehicle constructor")
        self.brand = brand


class Car(Vehicle):
    def __init__(self, fuel: str, brand: str) -> None:
        print("This is car constructor")
        super().__init__(brand)
        self.fuel = fuel

    def display(self):
        print(f"You have a {self.brand} car with {self.fuel} type")


car = Car("petrol", "maruti")
car.display()
