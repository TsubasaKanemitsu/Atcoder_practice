# 直積集合
# DFS

import itertools
n, x = list(map(int, input().split()))

inp = [list(map(int, input().split())) for _ in range(n)]

L = []
A = []

for i in range(n):
    L.append(inp[i][0])
    A.append(inp[i][1:])

ans = 0
# 袋に入っているボールの個数の総積は10 ** 5以下
for product in itertools.product(*A):
    num = 1
    for p in product:
        num *= p
    if num == x:
        ans += 1
    # print(product)
print(ans)