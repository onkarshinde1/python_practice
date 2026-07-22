class Student:
    school = "SD Jain Modern School"

    def __init__(self, name: str) -> None:
        self.name = name


s1 = Student("Anirudh")
s2 = Student("Priya")
print(s1.name)  # instance variables
print(s2.name)  # instance variables

print(s1.school)  # class variables
print(s2.school)  # class variables
print(Student.school)  # class variables

# 1st way to change class variables
Student.school = "XYZ"

print(s1.school)  # class variables
print(s2.school)  # class variables
print(Student.school)  # class variables
