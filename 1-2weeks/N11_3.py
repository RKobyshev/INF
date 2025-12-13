def TonySort(a):
    if not all(type(x) is type(a[0]) for x in a[1:]):return "TypeErr"
    if len(a)<=1:return a
    s = a[len(a)//2]
    l = [x for x in a if x < s]
    m = [x for x in a if x == s]
    r = [x for x in a if x > s]
    return TonySort(l) + m + TonySort(r)
assert TonySort([1, 2, 3]) == [1, 2, 3], f"{TonySort([1, 2, 3])} isnt[1,2,3]"
assert TonySort([1, "2", [3]]) == "TypeErr", "BRUH"
