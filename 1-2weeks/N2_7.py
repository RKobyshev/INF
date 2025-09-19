s = list(map(int, input().split()))
nmax = 0
cmax = 0
for i in s:
    if s.count(i) > cmax:
        nmax = i
        cmax = s.count(i)
print(nmax)