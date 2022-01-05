import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

# スタート地点を1 ~ Nとし、
# その地点から到着する都市毎にカウントすることで
# スタート地点とゴール地点の組み合わせを求めることができる。

n, m = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append(b)

cnt = 0
def dfs(v):
    global cnt
    if visited[v]:
        return
    visited[v] = True
    cnt += 1
    for e in graph[v]:
        if not visited[e]:
            dfs(e)

for i in range(n):
    visited = [False] * n
    dfs(i)
print(cnt)
