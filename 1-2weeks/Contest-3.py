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
class node:
    def __init__(self):
        self.leftn = 0
        self.leftf = 0
        self.rightn = 0
        self.rightf = 0
        self.maxn = 0
class ST:
    def __init__(self):
