f = open("input.txt").readlines()
a = [int(x) for x in f[0].split()]
sign = f[1][0]
N = int(f[2][0])
# print(a)
# print(sign)
# print(N)
n = 1
if sign =="+":
    n = sum(a)

if sign == "-":
    n = a[0]
    for i in range(1, len(a)):
        n -= a[i]
if sign == "*":
    n = a[0]
    for i in range(1, len(a)):
        n *= a[i]
print(n)
