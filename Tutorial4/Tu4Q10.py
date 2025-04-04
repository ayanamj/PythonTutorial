class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"
c1 = Complex(4,6)
c2 = Complex(1,5)
c3 = c1 + c2
print("Sum of complex numbers:", c3)
