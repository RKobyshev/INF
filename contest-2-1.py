# class g:
#     def __init__(self):self.adj={}
#     def add(self, u, v):
#         if u not in self.adj:self.adj[u]=[]
#         self.adj[u].append(v)
#     def dfs(self, st):
#         vis = set()
#         stak = [st]
#         while stak:
#             v = stak.pop()
#             if v not in vis:vis.add(v)
#             if v in self.adj:
#                 for i in range(len(self.adj[v])):
#                     stak.append(self.adj[v][i])
#         return vis
#
# n, m = map(int, input().split())
# gr = g()
# for i in range(n):
#     l, r = map(int, input().split())
#     gr.add(l, r)
# visited = gr.dfs(st=1)
# print(len(visited))
# for x in sorted(visited):print(x)


# class g:
#     def __init__(self, n):
#         self.adj = [[]for i in range(n)]
#         self.prem = [None]*n
#     def add(self, u, v):self.adj[u].append(v)
#     def dfs(self, v):
#         if self.prem[v] != None:return self.prem[v]
#         if not self.adj[v]: self.prem[v] = 1
#         else:
#             total = 0
#             for i in self.adj[v]:
#                 total+=self.dfs(i)
#             self.prem[v] = total
#         return self.prem[v]
#     def absolute(self):
#         for i in range(len(self.adj)):
#             if self.prem[i] is None: self.dfs(i)
#         return sum(self.prem)
#
# n = int(input())
# gr = g(n)
# for i in range(n):
#     l = input().strip()
#     for j in range(len(l)):
#         if l[j]=="Y":gr.add(i, j)
#
# print(gr.absolute())

# class g:
#     def __init__(self, n):self.adj = [[]for i in range(n)]
#     def add(self, u, v):
#         self.adj[u].append(v)
#         self.adj[v].append(u)
#     def concomp(self):
#         n = len(self.adj)
#         vis = set()
#         comps = []
#         for start in range(n):
#             if start in vis: continue
#             comp = []
#             stack = [start]
#             vis.add(start)
#             while stack:
#                 u = stack.pop()
#                 comp.append(u)
#                 for v in self.adj[u]:
#                     if v not in vis:
#                         vis.add(v)
#                         stack.append(v)
#             comps.append(comp)
#         return comps
#
# n, m = map(int, input().split())
# gr = g(n)
# r = []
# for i in range(m):
#     x, y = map(int, input().split())
#     x-=1
#     y-=1
#     gr.add(x, y)
#     r.append((x, y))
#
# comps = gr.concomp()
# iscompof = [-1]*n
# for i in range(len(comps)):
#     comp = comps[i]
#     for v in comp:iscompof[v] = i
#
# rc = [0]*len(comps)
# for u,v in r:rc[iscompof[u]] += 1
#
# cwithnoc = 0
# for i in range(len(comps)):
#     comp = comps[i]
#     if len(comp) == rc[i]+1:cwithnoc+=1
# print(cwithnoc)

# class g:
#     def __init__(self, n):
#         self.n = n
#         self.d = [[1000000000000] * n for j in range(n)]
#         for j in range(n):self.d[j][j] = 0
#     def add(self, u, v, w):
#         if self.d[u][v]>w:self.d[u][v]=w
#     def floyd(self):
#         for i in range(self.n):
#             for j in range(self.n):
#                 for k in range(self.n):
#                     if self.d[j][k] > self.d[i][k] + self.d[j][i]: self.d[j][k] = self.d[i][k]+self.d[j][i]
#         for i in range(self.n):
#             if self.d[i][i] < 0:return False
#         return True
#
# n,m = map(int, input().split())
# gr = g(n+1)
# for i in range(m):
#     ner = input().split()
#     l,r,ves,s = int(ner[0]) - 1, int(ner[1]), int(ner[2]), ner[3]
#     if s == "<=":gr.add(l, r, ves)
#     else: gr.add(r, l, -ves)
# if gr.floyd():print("YES")
# else:print("NO")

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1]*size
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] > self.rank[ry]: self.parent[ry] = rx
            elif self.rank[ry] > self.rank[rx]: self.parent[rx] = ry
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1
    def connected(self, x, y): return self.find(x) == self.find(y)

n, m, k = map(int, input().split())
for i in range(m):input()
o = []
for i in range(k):
    t, u, v = input().split()
    o.append((t, int(u) - 1, int(v) - 1))
d = DSU(n)
a = []
for t, u, v in reversed(o):
    if t=="ask":
        if d.connected(u, v):a.append("YES")
        else: a.append("NO")
    else: d.union(u, v)
a.reverse()
for i in a:print(i)