# 復習

import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict
n = int(input())
C = list(map(int, input().split()))

tree = defaultdict(list)

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * n
color_cnt = [0] * (10 ** 5 + 1)
ans = []

def dfs(v):
    if visited[v]:
        return
    if color_cnt[C[v]] == 0:
        ans.append(v + 1)
    visited[v] = True
    color_cnt[C[v]] += 1

    for e in tree[v]:
        if not visited[e]:
            dfs(e)
    color_cnt[C[v]] -= 1

dfs(0)


ans.sort()
for a in ans:
    print(a)