
f = open("f1", encoding='utf-8').read()
s = "аеиоуыэюя"
for i in range(1, len(f)-1):
    if f[i-1] not in s and f[i] in s:
        f = f[:i+1] + "с"+f[i] + f[i+1:]
        i = i+2
print(f)
#несмотря на попытки установки кодирровки, все равно выводится не то, что нужно