f = open("file").read()
n = 0
n += f.count("?!")
f = f.replace("?!", " ")
n+= f.count("...")
f = f.replace("...", " ")
n = n + f.count("!") + f.count("?") + f.count(".")
print(n)