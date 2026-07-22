class Student:
    def __init__(self, roll_no: int, name: str, gender: str, age: int) -> None:
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.age = age

    # Methods
    def display_details(self) -> None:
        print(f"Roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")


# Object/Instance
student1 = Student(1, "Anirudh", "Male", 88)
student1.display_details()
