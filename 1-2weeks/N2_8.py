def ismed(n, a):
    nm = 0
    nb = 0
    for i in a:
        if i<n:nm+=1
        if i>n:nb+=1
    if nm==nb:return True
    else:return False

n = int(input())
s = list(map(int, input().split()))
for i in s:
    if ismed(i, s):print(i)
