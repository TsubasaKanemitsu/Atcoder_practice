# ABC 145 C
# 10分
# 順列組み合わせの実装に手間取った


import itertools
import math
n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
dist = 0
for prod in itertools.permutations([i for i in range(n)]):
    cnt += 1
    for i in range(len(prod) - 1):
        ii = prod[i]
        jj = prod[i + 1]
        xi, yi = xy[ii]
        xj, yj = xy[jj]
        dist += math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

print(dist / cnt)
