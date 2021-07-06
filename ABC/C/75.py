import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

n, m = list(map(int, input().split()))

graph = [[False] * (n + 1) for _ in range(n + 1)]
AB = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    a, b = AB[i]
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (n + 1)

# ある一つの頂点からある頂点を通らない場合に、
# 他のすべての頂点を通ることができるかどうか
def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    for e in range(1, n + 1):
        # パスが通っていない場合
        if not graph[v][e]:
            continue
        # 既に到達済みの場合
        if visited[e]:
            continue
        dfs(e)


ans = 0
# 辺を1本ずつ外して考える
for i in range(m):
    a, b = AB[i]
    graph[a][b] = False
    graph[b][a] = False
    
    # 頂点の到達の管理
    visited = [False] * (n + 1)
    
    # 全ての頂点が連結しているかどうかを
    # 確認したいのでどこを頂点として始めてもいい
    dfs(1)

    # 橋がない
    bridge = False
    for j in range(1, n + 1):
        if not visited[j]:
            bridge = True
            break
    
    if bridge:
        ans += 1
    graph[a][b] = True
    graph[b][a] = True

print(ans)