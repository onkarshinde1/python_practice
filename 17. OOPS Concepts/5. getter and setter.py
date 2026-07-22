class Student:
    def __init__(self, name) -> None:
        self.__name = name

    # Getter
    def get_name(self):
        return self.__name

    # Setter
    def set_name(self, new_name: str):
        self.__name = new_name


s1 = Student("Anirudh")
print(s1.get_name())
s1.set_name("Xyz")
print(s1.get_name())
