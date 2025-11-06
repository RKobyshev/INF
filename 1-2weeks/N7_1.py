# class Vector:
#     def __init__(self, x = 0, y = 0, z = 0):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __abs__(self):
#         return (self.x**2 + self.y**2 + self.z**2)**0.5
#     def __add__(self, other):
#             x1, y1, z1 = self.x, self.y, self.z
#             x2, y2, z2 = other.x, other.y, other.z
#             res = Vector(x1+x2, y1+y2, z1+z2)
#             return res
#     def __scal__(self, other):
#         x1, y1, z1 = self.x, self.y, self.z
#         x2, y2, z2 = other.x, other.y, other.z
#         return (x1*x2 + y1*y2 + z1*z2)
#     def __mn__(self, n):
#         return Vector(self.x*n, self.y*n, self.z*n)
#     def __str__(self):return f"{self.x}, {self.y}, {self.z}"
# v1 = Vector(1, 2, 3)
# v2 = Vector(2, 3, 4)
# print(v1.__add__(v2).__str__())
# n = 4
# print(v1.__mn__(n).__str__())



s = "{1, 22, 354}"
print(s.find(','))
print(s.find(',', s.find(' ')))
print(s[1:s.find(',')])
print(s[s.find(',')+2:s.find(',', s.find(' '))])
print(s[s.find(',', s.find(' ')+1)+2:s.find('}')])

class v:
    def __init__(self, s):
        self.x = float(s[1:s.find(',')])
        self.y = float(s[s.find(',')+2:s.find(',', s.find(' '))])
        self.z = float(s[s.find(',', s.find(' ')+1)+2:s.find('}')])
    def __abs__(self):return (self.x**2 + self.y**2 + self.z**2)**0.5

v1 = v("{1, 2, 3}")
print(v1.__abs__())