class rect:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

l = float(input("Enter length: "))
w = float(input("Enter width: "))
rect = rect(l, w)
print("Area of Rectangle:", rect.area())
