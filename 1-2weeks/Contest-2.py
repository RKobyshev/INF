#1
# def sk(s):
#     st = []
#     for i in s:
#         if i in "([{": st.append(i)
#         else:
#             if i == ")":
#                 if not st or st[-1] != "(": return "No"
#                 st.pop()
#             if i == "]":
#                 if not st or st[-1] != "[": return "No"
#                 st.pop()
#             if i == "}":
#                 if not st or st[-1] != "{": return "No"
#                 st.pop()
#     if not st: return "Yes"
#     else: return "No"
#
# print(sk(input()))
#2
# n = int(input())
# o = []
# for i in range(n):
#     a, b = map(int, input().split())
#     o.append((a, b))
# o.sort(key= lambda x: x[1])
# c = 0
# last = -10000000000
# for l, r in o:
#     if l>last:
#         c+=1
#         last=r
# print(c)
#3
# k = int(input())
# for i in range(k):
#     n, m = map(int, input().split())
#     s = []
#     for j in range(m):s.append(input())
#     res = []
#     for elem in s:
#         c = 0
#         for x in range(n):
#             for y in range(x+1, n):
#                 if elem[x]>elem[y]: c+=1
#         res.append((c, elem))
#     res.sort(key= lambda x: x[0])
#     for a in res: print(a[1])
#     print()
#4
# import heapq
# n = int(input())
# a=[]
# for i in range(n):
#     t, d = map(int, input().split())
#     a.append((d, t))
# a.sort()
# h = []
# T = 0
# for d, t in a:
#     if T + t <= d:
#         heapq.heappush(h, -1*t)
#         T+=t
#     else:
#         if h and h[0] < (-1*t):
#             l = -1*heapq.heappop(h)
#             T = T - l + t
#             heapq.heappush(h, -1*t)
# print(len(h))
#5
s = input().split()
d = {}
for i in s:
    key = "".join(sorted(i))
    # print(key)
    if key not in d:d[key] = []
    d[key].append(i)
ks = list(d.keys())
ks.sort(key=lambda x:((-1*len(d[x])), min(x)))
res=[]
for i in ks:res.extend(sorted(d[i]))
print(" ".join(res))
#def dfe edf efd khn knh gln krc srp kte rrc kas hep erd sam obo cpk mil aha
#def dfe edf efd khn knh aha cpk erd gln hep kas krc kte mil obo rrc sam srp
#def dfe edf efd khn knh kas sam aha obo krc rrc cpk erd kte hep gln mil srp