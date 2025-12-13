import numpy as np
def MNK(x, y):
    X = np.array(x)
    Y = np.array(y)
    xm, ym = X.mean(), Y.mean()
    A = np.sum((X - xm)*(Y - ym))
    B = np.sum((X - xm)**2)
    if B!=0:a = A/B
    else: return "x - error"
    b = ym - a*xm
    return f"y = {a}x + {b}"

assert MNK([1,1,1], [1, 1, 1])=="x - error", "Cannot solve"
assert MNK([1,2,3], [1, 2, 3])=="y = 1.0x + 0.0", "Error in formula"
