# LCA(Lowest Common Ancestor)
# 最小共通祖先
# https://algo-logic.info/lca/

from collections import defaultdict
n, m = list(map(int, input().split()))

tree = defaultdict(int)

for _ in range(m):
    a, b = list(map(int, input().split()))
    tree[a] += 1
    tree[b] += 1

for k, v in tree.items():
    if v % 2 == 1:
        print("NO")
        exit()
print("YES")
