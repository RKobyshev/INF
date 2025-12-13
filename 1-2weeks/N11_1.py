def NtoP(n):
    res = []
    if n<0:return "SIGN_ERR"
    if n==0:return "Cannot solve"
    while n%2==0:
        res.append(2)
        n//=2
    i=3
    while i**2 <= n:
        while n%i==0:
            res.append(i)
            n//=i
        i+=2
    if n>1: res.append(n)
    res.sort()
    return res

assert NtoP(2)==[2], f"{NtoP(2)} must be [2]"
assert NtoP(97)==[97], f"{NtoP(97)} must be [97]"
assert NtoP(10)==[2, 5], f"{NtoP(10)} must be [2,5]"
assert NtoP(81)==[3,3,3,3], f"{NtoP(81)} must be [3,3,3,3]"
assert NtoP(-1)=="SIGN_ERR", "Cannot work with n<0"
assert NtoP(0)=="Cannot solve", "0 isnt p"