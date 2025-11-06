class Complex:
    def __init__(self, re=0, im=0):
        self.re=re
        self.im = im
    def __add__(self, other):
        re1 = self.re
        re2 = other.re
        im1 = self.im
        im2 = other.im
        result = Complex(re1+re2, im1+im2)
        return result
    def __mul__(self, other):
        re1 = self.re
        re2 = other.re
        im1 = self.im
        im2 = other.im
        result = Complex(re1*re2 - im1*im2, re1*im2 + re2*im1)
        return result
    def __str__(self):
        re = self.re
        im = self.im
        result = f"{re} + {im}i"
        return result
    def __abs__(self):return (self.re)**2+(self.im)**2

c1 = Complex(1, 2)
c2 = Complex(4, 5)
print(c1.__add__(c2))
print(c1.__mul__(c2))
print(c1.__abs__())
print(c1.__str__())