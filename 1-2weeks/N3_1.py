from functools import lru_cache
@lru_cache(None)
def fib(n):
    if n == 1: return 0
    if n == 2: return 1
    else: return fib(n-1) + fib(n-2)


fib(100)

print(fib(100))
