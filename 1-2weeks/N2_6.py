# s = [1,2,3,1]
# print(s.count(1))
s = list(map(int, input().split()))
for i in s:
    if s.count(i)==1:print(i)