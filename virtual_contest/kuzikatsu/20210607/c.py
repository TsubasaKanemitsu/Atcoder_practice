from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
n, m = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)


def dfs(i, visited):
    if visited[i]:
        return
    visited[i] = True
    for e in graph[i]:
        if not visited[e]:
            dfs(e, visited)


ans = 0
for i in range(n):
    visited = [False] * n
    dfs(i, visited)
    ans += sum(visited)
print(ans)