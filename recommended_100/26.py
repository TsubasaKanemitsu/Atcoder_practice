from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

n, q = list(map(int, input().split()))

tree = defaultdict(list)
cnt = [0] * (n + 1)

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)


def dfs(v, x, visited):
    visited.add(v)
    cnt[v] += x
    for i in tree[v]:
        if i not in visited:
            dfs(i, x, visited)


for _ in range(q):
    p, x = list(map(int, input().split()))
    visited = set()
    dfs(p, x, visited)

for i in range(1, n + 1):
    print(cnt[i], end=' ')
print()