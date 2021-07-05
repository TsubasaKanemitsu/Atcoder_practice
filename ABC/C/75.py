# Union Find木
from collections import defaultdict
n, m = list(map(int, input().split()))

graph = defaultdict(list)
cnt = defaultdict(int)
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

print(graph)
def dfs(v, visited):
    
    if visited[v]:
        return

    visited[v] = True

    for e in graph[v]:
        if visited[e]:
            continue
        dfs(e, visited)


ans = 0
for i in range(1, n + 1):
    if len(graph[i]) == 1:
        print(i, graph[i])
        ans += 1
    for e in graph[i]:
        for e2 in graph[i]:
            visited = [False] * (n + 1)
            if e2 == e:
                continue
            visited[i] = True
            dfs(e2, visited)
            print(i, visited, e2, e)
            if not visited[e]:
                print("cnt")
                cnt[(min(i, e), max(i, e))] += 1

print(cnt)