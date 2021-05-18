from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

graph = defaultdict(list)

for _ in range(n):
    a = list(map(int, input().split()))
    if a[1] > 0:
        graph[a[0]].extend(a[2:])

visited = [False] * (n + 1)
d = [0] * (n + 1)
f = [0] * (n + 1)


def dfs(v):
    global current_time
    d[v] = current_time
    current_time += 1
    
    for i in graph[v]:
        if visited[i]:
            continue
        visited[i] = True
        dfs(i)
    
    f[v] = current_time
    current_time += 1
    

current_time = 1
for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = True
        dfs(i)

for i in range(1, n + 1):
    print(i, d[i], f[i])