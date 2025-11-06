class cat:
    def __init__(self, breed, color, age):
        self.breed = breed
        self.__color = color
        self.age = age
    def getbreed(self):
        return self.breed
    def setcolor(self, newcolor):
        self.__color = newcolor
    def getcolor(self):return self.__color

    def __add__(self, other):
        breed1=self.breed
        breed2=other.breed
        color1 = self.__color
        color2 = other.__color
        newcat=cat((breed1+breed2)//2, (color1+color2)//2, 0)
        return newcat

a1 = cat(1, 2, 3)
# print(a1)
print(cat.getbreed(a1))
a = a1.breed
print(a)
a1.setcolor(5)
print(a1.getcolor())
a2 = cat(3,  6,  2)
a3 = a1.__add__(a2)
print(a3.breed)
