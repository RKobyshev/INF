# def custom_sum(*args):
#     s = 0
#     for v in args:
#         s += v
#     return s
#
#
# def test_custom_sum():
#     assert custom_sum(1, 2, 3, 4, 5) == 15, "should be 15"
#     assert custom_sum() == 0, "should be 0"
#     assert custom_sum(0) == 0, "should be 0"
#     assert custom_sum(1, -1) == 0, "should be 0"
#
# test_custom_sum()


def isp(n):
    if n==2:return True
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True
def ntop(n):
    result = []
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            result.append(i)
            result.append(n//i)
            n//=i
    return result.sort()
assert ntop(2)==[2], f"{ntop(2)}, but must be 2"
assert ntop(10)==[2, 5], f"{ntop(2)}, but must be [2, 5]"