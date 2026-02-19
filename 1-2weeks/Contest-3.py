#1
# def checkbst(tree, i, dopmin, dopmax):
#     if i >= len(tree) or tree[i] == None: return True
#     Ti = tree[i]
#     if Ti <= dopmin or Ti >= dopmax: return False
#     l, r = 2*i + 1, 2*i + 2
#     return (checkbst(tree, l, dopmin, Ti)) and (checkbst(tree, r, Ti, dopmax))
#
# elems = input().split()
# tree = []
# for i in elems:
#     if i == "None":tree.append(None)
#     else: tree.append(int(i))
# if checkbst(tree, 0, -10**10, 10**10):print("YES")
# else: print("NO")
#2
# class node:
#     def __init__(self, HA):
#         self.data = HA
#         self.left, self.right = None, None
#
# class BST:
#     def __init__(self): self.root = None
#     def insert(self, HA):
#         new = node(HA)
#         if self.root == None:
#             self.root = new
#             return
#         old = self.root
#         while True:
#             if new.data[0] < old.data[0]:
#                 if old.left == None:
#                     old.left = new
#                     return
#                 old = old.left
#             else:
#                 if old.right == None:
#                     old.right = new
#                     return
#                 old = old.right
#     def search(self, key):
#         n = self.root
#         while n != None:
#             if key == n.data[0]: return n.data[1]
#             if key < n.data[0]: n = n.left
#             if key > n.data[0]: n = n.right
#         return None
#
# tree = BST()
# n = int(input())
# for i in range(n):
#     hero, art = input().split()
#     tree.insert((hero, art))
#     tree.insert((art, hero))
# q = int(input())
# for i in range(q):
#     s = input()
#     print(tree.search(s))
#3
# class node:
#     def __init__(self, leftn = 0, leftf = 0, rightn = 0, rightf = 0, maxf = 0):
#         self.leftn = leftn
#         self.leftf = leftf
#         self.rightn = rightn
#         self.rightf = rightf
#         self.maxf = maxf
#         self.left, self.right = None, None
# class ST:
#     def __init__(self, a):
#         self.n = len(a)
#         self.root = self.build(a, 0, self.n - 1)
#     def build(self, a, l, r):
#         if l==r:
#             v = a[l]
#             return node(leftn=v, leftf=1, rightn=v, rightf=1, maxf=1)
#         m = (l+r)//2
#         left = self.build(a, l, m)
#         right = self.build(a, m+1, r)
#         N = self.merge(left, right)
#         N.left, N.right = left, right
#         return N
#     def merge(self, left, right):
#         N = node()
#         N.leftn = left.leftn
#         N.rightn = right.rightn
#         if left.leftn == right.leftn: N.leftf = left.leftf + right.leftf
#         else: N.leftf = left.leftf
#         if right.rightn == left.rightn: N.rightf = right.rightf + left.rightf
#         else: N.rightf = right.rightf
#         N.maxf = max(left.maxf, right.maxf)
#         if left.rightn == right.leftn: N.maxf = max(N.maxf, left.rightf + right.leftf)
#         return N
#     def res(self, l, r):
#         def resR(N, L, R, l, r):
#             if N == None: return None
#             if l<=L and R<=r:return N
#             if r<L or R<l:return None
#             M = (L+R)//2
#             leftres = resR(N.left, L, M, l, r)
#             rightres = resR(N.right, M+1, R, l, r)
#             if leftres==None:return rightres
#             if rightres==None:return leftres
#             # if leftres==None and rightres==None: return None
#             return self.merge(leftres, rightres)
#         result = resR(self.root, 0, self.n - 1, l, r)
#         return result.maxf if result else 0
#
# t = int(input())
# for i in range(t):
#     n, q = map(int, input().split())
#     a = list(map(int, input().split()))
#     tree = ST(a)
#     for j in range(q):
#         m, l = map(int, input().split())
#         print(tree.res(m-1, l-1))
#5
# class ST:
#     def __init__(self, N, a):
#         self.N = N
#         self.size=1
#         while self.size < N:self.size*=2
#         self.tree = [0]*(2*self.size)
#         self.after = [-1]*(2*self.size)
#         for i in range(N):self.tree[self.size + i] = a[i]
#         for i in range(self.size - 1, 0, -1):self.tree[i] = self.tree[2*i]+self.tree[2*i + 1]
#     def tonode(self, n, v, l):
#         self.tree[n] = v*l
#         if n < self.size: self.after[n] = v
#     def damnit(self, n, l):
#         if self.after[n] != -1:
#             v = self.after[n]
#             k = l//2
#             leftl, rightl = l//2, l - k
#             self.tonode(2*n, v, leftl)
#             self.tonode(2*n + 1, v, rightl)
#             self.after[n]=-1
#     def update(self, n, nl, nr, l, r, v):
#         if l<=nl and nr<=r:
#             self.tonode(n, v, nr-nl+1)
#             return
#         if r<nl or l>nr:return
#         self.damnit(n, nr-nl+1)
#         m = (nl+nr)//2
#         self.update(2*n, nl, m, l, r, v)
#         self.update(2*n + 1, m+1, nr, l, r, v)
#         self.tree[n] = self.tree[2*n]+self.tree[2*n+1]
#     def summSEG(self, n, nl, nr, l, r):
#         if l<=nl and nr<=r:return self.tree[n]
#         if r<nl or l>nr:return 0
#         self.damnit(n, nr-nl+1)
#         m = (nl+nr)//2
#         return self.summSEG(2*n, nl, m, l, r) + self.summSEG(2*n+1, m+1, nr, l, r)
#     def set(self, l, r, v): self.update(1, 0, self.size-1, l, r, v)
#     def summ(self, l, r): return self.summSEG(1, 0, self.size-1, l, r)
#     def get(self, i):
#         return self.summ(i, i)
#
#
# n, q = map(int, input().split())
# s = input()
# FARMIM_LES = []
# for i in "abcdefghijklmnopqrstuvwxyz":
#     a = [0]*n
#     for j in range(n):
#         if s[j]==i: a[j]=1
#     tree = ST(n, a)
#     FARMIM_LES.append(tree)
# for i in range(q):
#     data = input().split()
#     l, r, d = int(data[0])-1, int(data[1])-1, int(data[2])
#     b = [0]*26
#     for j in range(26):b[j] = FARMIM_LES[j].summ(l, r)
#     for j in range(26):
#         if  b[j]:FARMIM_LES[j].set(l, r, 0)
#     now = l
#     if d:
#         for j in range(26):
#             if b[j]:
#                 FARMIM_LES[j].set(now, now + b[j] - 1, 1)
#                 now += b[j]
#     else:
#         for j in range(25, -1, -1):
#             if b[j]:
#                 FARMIM_LES[j].set(now, now + b[j] - 1, 1)
#                 now+=b[j]
# res = []
# c = "abcdefghijklmnopqrstuvwxyz"
# for i in range(n):
#     for j in range(26):
#         if FARMIM_LES[j].get(i):
#             res.append(c[j])
#             break
# RES = ''.join(res)
# print(RES)

n, q = map(int, input().split())
s = input()
alphabet = 26
size = 1
while size < n:
    size *= 2
size *= 2
sumt = [[0] * (2 * size) for _ in range(alphabet)]
lazy = [[-1] * (2 * size) for _ in range(alphabet)]
for i in range(n):
    c = ord(s[i]) - 97
    sumt[c][size + i] = 1
for ch in range(alphabet):
    for i in range(size - 1, 0, -1):
        sumt[ch][i] = sumt[ch][2*i] + sumt[ch][2*i + 1]
        lazy[ch][i] = -1
def push(ch, v, l_len, r_len):
    if lazy[ch][v] != -1:
        tag = lazy[ch][v]
        left_child = 2 * v
        right_child = 2 * v + 1
        sumt[ch][left_child] = tag * l_len
        sumt[ch][right_child] = tag * r_len
        if left_child < size:
            lazy[ch][left_child] = tag
        if right_child < size:
            lazy[ch][right_child] = tag
        lazy[ch][v] = -1
def update(ch, v, vl, vr, l, r, val):
    if l > r:
        return
    if l == vl and r == vr:
        sumt[ch][v] = val * (vr - vl + 1)
        if v < size:
            lazy[ch][v] = val
        return
    mid = (vl + vr) // 2
    left_len = mid - vl + 1
    right_len = vr - mid
    if v < size:
        push(ch, v, left_len, right_len)
    if r <= mid:
        update(ch, 2*v, vl, mid, l, r, val)
    elif l > mid:
        update(ch, 2*v+1, mid+1, vr, l, r, val)
    else:
        update(ch, 2*v, vl, mid, l, mid, val)
        update(ch, 2*v+1, mid+1, vr, mid+1, r, val)
    sumt[ch][v] = sumt[ch][2*v] + sumt[ch][2*v+1]
def query(ch, v, vl, vr, l, r):
    if l > r:
        return 0
    if l == vl and r == vr:
        return sumt[ch][v]
    mid = (vl + vr) // 2
    left_len = mid - vl + 1
    right_len = vr - mid
    if v < size:
        push(ch, v, left_len, right_len)
    if r <= mid:
        return query(ch, 2*v, vl, mid, l, r)
    elif l > mid:
        return query(ch, 2*v+1, mid+1, vr, l, r)
    else:
        return (query(ch, 2*v, vl, mid, l, mid) +
                query(ch, 2*v+1, mid+1, vr, mid+1, r))
for j in range(q):
    data = input().split()
    l, r, k = int(data[0]) - 1, int(data[1]) - 1, int(data[2])
    cnt = [0] * 26
    for ch in range(26):
        cnt[ch] = query(ch, 1, 0, size-1, l, r)
    for ch in range(26):
        update(ch, 1, 0, size-1, l, r, 0)
    now = l
    if k == 1:
        for ch in range(26):
            if cnt[ch]:
                update(ch, 1, 0, size-1, now, now + cnt[ch] - 1, 1)
                now += cnt[ch]
    else:
        for ch in range(25, -1, -1):
            if cnt[ch]:
                update(ch, 1, 0, size-1, now, now + cnt[ch] - 1, 1)
                now += cnt[ch]
res = [''] * n
for ch in range(26):
    stack = [(1, 0, size-1)]
    letter = chr(ord('a') + ch)
    while stack:
        v, l, r = stack.pop()
        if l >= n or r < 0:
            continue
        if lazy[ch][v] != -1:
            if lazy[ch][v] == 1:
                start = max(l, 0)
                end = min(r, n-1)
                for i in range(start, end + 1):
                    res[i] = letter
            continue
        if l == r:
            if sumt[ch][v] == 1 and l < n:
                res[l] = letter
            continue
        m = (l + r) // 2
        stack.append((2*v+1, m+1, r))
        stack.append((2*v, l, m))
print(''.join(res))