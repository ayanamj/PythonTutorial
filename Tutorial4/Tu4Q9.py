#In Python, a class is instantiated by creating an object of the class by calling the class name followed by ().
#Syntax : object_name = ClassName()


class Rectangle:
    def __init__(self, height, width, xcorner, ycorner):
        self.height = height
        self.width = width
        self.xcorner = xcorner
        self.ycorner = ycorner
    def center(self):
        xcenter = self.xcorner + self.width / 2
        ycenter = self.ycorner + self.height / 2
        return (xcenter, ycenter)
    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)
rect = Rectangle(5, 2, 3, 1)
print("Center:", rect.center())
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
