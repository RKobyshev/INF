def isp(p):
    if p == 0: return False
    if p == 1: return False
    if p == 2: return True
    for i in range(2, int(p**(0.5))+1):
        if p%i == 0:return False
    return True

def pn(n):return [int(x) for x in range(n) if isp(x)]

def power(n, x):
    p = 0
    while n%x == 0:
        n//=x
        p+=1
    return p

def krosivoe(s):
    a = ""
    for i in s: a += "(" + str(i[0]) + "^" + str(i[1]) + ")"
    return a

n = int(input())
p = pn(n)
res = []
for i in p:
    if n%i == 0:res.append([i, power(n, i)])
print(res)
print(krosivoe(res))

