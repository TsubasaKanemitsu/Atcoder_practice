# 再帰関数 DFS
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

n, q = list(map(int, input().split()))

AB = [list(map(int, input().split())) for _ in range(n - 1)]
PX = [list(map(int, input().split())) for _ in range(q)]

tree = defaultdict(list)

for a, b in AB:
    tree[a].append(b)
    tree[b].append(a)

cnt = defaultdict(int)

for p, x in PX:
    cnt[p] += x

visited = [False] * (n + 1)
point = [0] * (n + 1)


def dfs(v, now_point):
    visited[v] = True
    point[v] = now_point
    for e in tree[v]:
        if not visited[e]:
            dfs(e, now_point + cnt[e])


dfs(1, cnt[1])

for i in range(1, n + 1):
    print(point[i], end=" ")