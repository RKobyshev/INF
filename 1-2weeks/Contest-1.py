# N, M = map(int, input().split())
#
# x = list(map(int, input().split()))
# y = list(map(int, input().split()))
# dp = [[0]*(M+1) for _ in range(N+1)]
# res = [0]+x
# p = [0]+y
# for i in range(1,N+1):
#     for j in range(1, M+1):
#         if res[i]>j: dp[i][j] = dp[i-1][j]
#         else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-res[i]] + p[i])
# print(dp[N][M])


# def dev(n, m):
#     if (n%2)*(m%2)==0: return 0
#     else:return 1 + 4*dev(n//2, m//2)
#
# n, m = map(int, input().split())
# print(dev(n, m))

# a, b = map(int, input().split())
# for x in range(0, 200000):
#     if ((a+x)%b) == ((b+x)%a) == 0:
#         print(x)
#         break

# n, k = map(int, input().split())
# A = list(map(int, input().split()))
# b = []
# for i in range(2**n):
#     j = i^k
#     b.append(A[i]+A[j])
# print(max(b))

# print(int("-1"))

# def maxdev(s):
#     try:
#         return int(s), int(s)
#     except:
#         maxres = float('-inf')
#         minres = float('inf')
#         for i in range(len(s)):
#             sign = s[i]
#             if sign in "+-*":
#                 l = s[:i]
#                 r = s[i+1:]
#                 lmax, lmin = maxdev(l)
#                 rmax, rmin = maxdev(r)
#                 if sign == "+": var = [lmin+rmin, lmin+rmax, lmax+rmin, lmax+rmax]
#                 if sign == "-": var = [lmin-rmin, lmin-rmax, lmax-rmin, lmax-rmax]
#                 if sign == "*": var = [lmin*rmin, lmin*rmax, lmax*rmin, lmax*rmax]
#                 maxres = max(*var, maxres)
#                 minres = min(*var,minres)
#
#     return maxres, minres
#
# print(maxdev(input())[0])


def F(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(0, i):
            dp[i][j] = dp[i - 1][j]
        for j in range(i, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i // 2][j - i]

    return (dp[n][n])
print(F(int(input())))