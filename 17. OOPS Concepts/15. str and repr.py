class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


p1 = Point(3, 4)
p2 = Point(65, 11)
print(p1)
print(p2)
print(repr(p1))
print(repr(p2))
