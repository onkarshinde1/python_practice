class Student:
    def __init__(self, name: str, age: int, marks: list[int]) -> None:
        self.name: str = name
        self.age: int = age
        self.marks: list[int] = marks

    def total(self) -> int:
        return sum(self.marks)

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def grade(self) -> None:
        avg = self.average()
        if avg >= 90:
            print("A")
        elif avg >= 50 and avg <= 89:
            print("B")
        else:
            print("C")


student1 = Student("Anirudh", 67, [78, 54, 19, 63])
total = student1.total()
print(total)
avg = student1.average()
print(avg)
student1.grade()
