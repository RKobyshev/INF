def pr(a):
    x = 1
    for i in a: x*=i
    return x

a = list(map(int, input().split()))
print(pr(a)**(1/len(a)))
