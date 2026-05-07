# import heapq
# class G:
#     def __init__(self, n):
#         self.n = n
#         self.adj = [[] for i in range(n)]
#     def add(self, u, v, w):
#         self.adj[u].append((v, w))
#         self.adj[v].append((u, w))
#     def D(self, st):
#         inf = 100000000
#         dist = [inf] * self.n
#         dist[st] = 0
#         dv = [(0, st)]
#         while dv:
#             d, v = heapq.heappop(dv)
#             if d > dist[v]: continue
#             for to, w in self.adj[v]:
#                 ndv = d + w
#                 if ndv < dist[to]:
#                     dist[to] = ndv
#                     heapq.heappush(dv, (ndv, to))
#         return dist
#
# n, m, k = map(int, input().split())
# p = list(map(int, input().split()))
# p = [x-1 for x in p]
# graf = G(n)
# for i in range(m):
#     u, v, w = map(int, input().split())
#     graf.add(u - 1, v - 1, w)
# sd = [0]*n
# for s in p:
#     dist = graf.D(s)
#     for i in range(n): sd[i] += dist[i]
# bc = 0
# bsum = sd[0]
# for i in range(1, n):
#     if sd[i] < bsum:
#         bsum = sd[i]
#         bc = i
#     elif sd[i] == bsum and i < bc:bc = i
# print(bc+1, bsum)


# import heapq
# class G:
#     def __init__(self, n):
#         self.n = n
#         self.adj = [[] for i in range(n)]
#     def add(self, u, v, w): self.adj[u].append((v, w))
#     def D(self, st):
#         inf = 10000000
#         dist = [inf] * self.n
#         dist[st] = 0
#         dv = [(0, st)]
#         while dv:
#             d, v = heapq.heappop(dv)
#             if d > dist[v]:continue
#             for to, w in self.adj[v]:
#                 ndv = d + w
#                 if ndv < dist[to]:
#                     dist[to] = ndv
#                     heapq.heappush(dv, (ndv, to))
#         return dist
# n = int(input())
# e = int(input()) - 1
# t = int(input())
# m = int(input())
# graf = G(n)
# for i in range(m):
#     a, b, w = map(int, input().split())
#     a-=1
#     b-=1
#     graf.add(b, a, w)
# dist = graf.D(e)
# print(sum(1 for d in dist if d <= t))

# import heapq
# class G:
#     def __init__(self, n):
#         self.n = n
#         self.adj = [[] for i in range(n)]
#     def add(self, u, v, otpr, prib):self.adj[u].append((v, otpr, prib))
#     def D(self, fr, to):
#         inf = 10000000
#         dist = [inf]*self.n
#         dist[fr] = 0
#         dv = [(0, fr)]
#         while dv:
#             t, u = heapq.heappop(dv)
#             if t > dist[u]: continue
#             for v, otpr, prib in self.adj[u]:
#                 if t <= otpr and prib < dist[v]:
#                     dist[v] = prib
#                     heapq.heappush(dv, (prib, v))
#         return dist[to]
# n, e, m = map(int, input().split())
# e-=1
# graf = G(n)
# for i in range(m):
#     p = list(map(int, input().split()))
#     k = p[0]
#     st = []
#     for j in range(k):st.append((p[2*j+ 1] - 1, p[2*j + 2]))
#     for j in range(k-1):
#         u, tu = st[j]
#         v, tv = st[j+1]
#         graf.add(u, v, tu, tv)
# a = graf.D(0, e)
# if a == 10000000: print(-1)
# else: print(a)

# class DSU:
#     def __init__(self, size):
#         self.parent = list(range(size))
#         self.rank = [1] * size
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#
#         if rootX != rootY:
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.parent[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.parent[rootX] = rootY
#             else:
#                 self.parent[rootY] = rootX
#                 self.rank[rootX] += 1
#
#     def connected(self, x, y):
#         return self.find(x) == self.find(y)
# def damn_i_have_python_314():
#     n, m, p = map(int, input().split())
#     bad = set()
#     if p:
#         for x in map(int, input().split()):bad.add(x-1)
#     r = []
#     for i in range(m):
#         u, v, w = map(int, input().split())
#         r.append((u-1, v-1, w))
#     if len(bad) == n:
#         if n==1:print(0)
#         if n==2:
#             cost = 0
#             for u, v, w in r:
#                 if (u==0 and v==1) or (u==1 and v==0):
#                     cost = w
#                     break
#             print(cost if cost else "impossible")
#         else: print("impossible")
#         return
#     good = [i for i in range(n) if i not in bad]
#     dsu = DSU(n)
#     ge = sorted([(w, u, v) for u, v, w in r if u not in bad and v not in bad])
#     c = 0
#     for w, u, v in ge:
#         if not dsu.connected(u, v):
#             dsu.union(u, v)
#             c+=w
#     root = dsu.find(good[0])
#     for v in good[1:]:
#         if dsu.find(v)!=root:
#             print("impossible")
#             return
#     me = [10000000]*n
#     for u, v, w in r:
#         if u in bad and v not in bad and w < me[u]:me[u]=w
#         if v in bad and u not in bad and w < me[v]:me[v]=w
#     t=c
#     for b in bad:
#         if me[b]==10000000:
#             print("impossible")
#             return
#         t+=me[b]
#     print(t)
# damn_i_have_python_314()

# def bipartite(graph):
#     n = len(graph)
#     colors = [-1] * n
#     for start in range(n):
#         if colors[start] == -1:
#             queue = [start]
#             colors[start] = 0
#             while queue:
#                 u = queue.pop(0)
#                 for v in graph[u]:
#                     if colors[v] == -1:
#                         colors[v] = 1 - colors[u]
#                         queue.append(v)
#                     elif colors[v] == colors[u]:
#                         return False, []
#     set1 = [i for i in range(n) if colors[i] == 0]
#     set2 = [i for i in range(n) if colors[i] == 1]
#     return True, (set1, set2)
#
# def kuhn(graph):
#     n = len(graph)
#     match = [-1] * n
#     visited = [False] * n
#     _, parts = bipartite(graph)
#     L = parts[0]
#     def dfs(v):
#         for u in graph[v]:
#             if not visited[u]:
#                 visited[u] = True
#                 if match[u] == -1 or dfs(match[u]):
#                     match[u] = v
#                     return True
#         return False
#     max_matching = 0
#     for v in L:
#         visited = [False] * n
#         if dfs(v):
#             max_matching += 1
#     return max_matching
# n = int(input())
# for v in range(n):
#     r, c, k = map(int, input().split())
#     crd = list(map(int, input().split()))
#     b = set()
#     for i in range(k):
#         x = crd[2*i]
#         y = crd[2*i+1]
#         b.add((x, y))
#     graph = [[] for р in range(r + c)]
#     for i in range(r):
#         for j in range(c):
#             if (i, j) not in b:
#                 graph[i].append(r + j)
#                 graph[r + j].append(i)
#     print(kuhn(graph))

