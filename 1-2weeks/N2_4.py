s = list(map(int, input().split()))
for i in range(0, (len(s)//2)+1, 2):s[i],s[i+1] = s[i+1], s[i]
print(s)