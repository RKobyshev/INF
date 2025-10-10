f = open('pylic.txt').read().replace(".", " ").lower().split()
wd = {}
for i in f:
    if i in wd.keys():wd[i]+=1
    else:wd[i]=1
print(wd)
b=[]
for k in wd.keys():b.append(wd[k])
a = set(b)
i=0
while i < 10:
    for k in wd.keys():
        if wd[k] == max(a):
            print(k, wd[k])
            i+=1
    a.remove(max(a))
