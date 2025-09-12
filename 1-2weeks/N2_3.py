def ismirr(s, dict):
    fl = 0
    for i in range(len(s)):
        if s[i] != dict[s[-(i+1)]]:fl+=1
    if fl==0:return True

mirror = {"A": "A", "H":"H", "I":"I", "O":"O", "T":"T", "U":"U", "V":"V", "W":"W", "X":"X", "Y":"Y", "1":"1", "8":"8", "E":"3", "J":"L", "S":"2", "Z":"5", "3":"E", "L":"J", "2":"S", "5":"Z"}
s = str(input())
flag1 = 0
flag2 = 0
if s == s[::-1]:flag1+=1
if ismirr(s, mirror):flag2+=1
if flag1 == flag2 == 0:print(f"{s} is not a palindrome")
if flag1 == 1 and flag2 == 0:print(f"{s} is a regular palindrome")
if flag1 == 0 and flag2 == 1:print(f"{s} is a mirrored str")
if flag1 == 1 and flag2 == 1:print(f"{s} is a mirrored palindrome")