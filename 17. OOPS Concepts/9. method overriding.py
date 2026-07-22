class Animal:
    def speak(self):
        print("Animal is speaking")

    def display(self):
        print("This is a display function")


class Dog(Animal):
    def speak(self):
        super().speak()
        self.display()
        print("Dog is braking")


d = Dog()
d.speak()
