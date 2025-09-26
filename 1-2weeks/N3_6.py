from numpy import *

# def mnk(x, y):return (x@y)/(y@y)
# x = array([1, 2, 3])
# y = array([4, 5, 6])
# print(mnk(x, y))

def mnk1(x, y):
    b = ((x*y).mean() - x.mean()*y.mean())/((x*x).mean() - x.mean()**2)
    a = 