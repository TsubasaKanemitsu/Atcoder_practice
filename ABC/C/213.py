# ABC C 213
# 座標圧縮
from collections import defaultdict
h, w, n = list(map(int, input().split()))

A = []
B = []

for i in range(n):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    A.append(a)
    B.append(b)

AA = list(set(A))
BB = list(set(B))

AA.sort()
BB.sort()

a_dict = defaultdict(int)
b_dict = defaultdict(int)

for i in range(len(AA)):
    a = AA[i]
    a_dict[a] = i

for i in range(len(BB)):
    b = BB[i]
    b_dict[b] = i

for i in range(n):
    a = A[i]
    b = B[i]
    print(a_dict[a] + 1, b_dict[b] + 1)