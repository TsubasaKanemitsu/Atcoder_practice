# トポロジカルソート

from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n, m = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)


path = [0] * (n + 1)
visited = [False] * (n + 1)


def f(s):
    if visited[s]:
        return path[s]
    
    visited[s] = True
    cnt = 0
    for e in graph[s]:
        cnt = max(cnt, f(e) + 1)
    path[s] = cnt
    # メモ化しながらreturn
    return path[s]


ans = 0
for i in range(1, n + 1):
    ans = max(ans, f(i))
print(ans)