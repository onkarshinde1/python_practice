class Shape:
    def area(self):
        return 0    # default

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

shapes = [Rectangle(3, 4), Circle(5), Rectangle(2, 6)]
for s in shapes:
    print(s.area())     # 12, 78.5, 12
