class Arearectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area_of_rectangle(self):
        print("Length of the rectangle is : ", self.length)
        print("Breadth of the rectangle is : ", self.breadth)
        area = self.length * self.breadth
        print("Area of the rectangle is : ", area)
a = Arearectangle(20,30)
a.area_of_rectangle()