from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

visited = [False] * n
ans = []

def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    # ans.append(v + 1)
    ans.append(v + 1)
    for e in graph[v]:
        if not visited[e]:
            dfs(e)
            ans.append(v + 1)

dfs(0)
print(*ans)