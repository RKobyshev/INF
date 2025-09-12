def ntob(n, b):
    a = ""
    digs = "0123456789"
    while n:
        a = digs[n%b]+a
        n//=b
    return a

