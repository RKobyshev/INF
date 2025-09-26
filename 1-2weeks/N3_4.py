def ap(s, a):
    for i in range(len(a)):
        a[i] = s+ a[i]
    return a

def tr(size, s):
    res = []
    if size == 1:
        res.append(s)
    else:
        res.append(s)
        for i in ap(s, tr(size - 2, s)):
            res.append(i)
        res.append(s)
    return res

s = str(input())
n = int(input())
a = tr(n, s)
print(a)
for i in a:print(i)