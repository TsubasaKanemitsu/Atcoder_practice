# ABC 213 D: Takahashi Tour
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

graph = defaultdict(list)

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

arrived = []


def dfs(now, pre):
    arrived.append(now)
    for nxt in graph[now]:
        if nxt != pre:
            dfs(nxt, now)
            arrived.append(now)


dfs(1, -1)
print(*arrived)