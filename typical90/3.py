# 典型90 problem. 3
# ★4 自力AC

import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

n = int(input())

graph = defaultdict(list)

for i in range(n - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n + 1)
dist = [0] * (n + 1)

def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    for e in graph[v]:
        if visited[e]:
            continue
        dist[e] = dist[v] + 1
        dfs(e)

dfs(1)

idx = 1
max_val = dist[1]
for i in range(2, n + 1):
    if max_val < dist[i]:
        idx = i
        max_val = dist[i]

dist = [0] * (n + 1)
visited = [False] * (n + 1)
dfs(idx)
print(max(dist) + 1)