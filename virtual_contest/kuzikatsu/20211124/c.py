# 60min

# DFS
import sys
sys.setrecursionlimit(10 ** 7)


n = int(input())
TKA = [list(map(int, input().split())) for _ in range(n)]

# 技はN個
# 技iの習得には時間Ti必要
# 修練開始時点でAi,1 ~ Ai,kiを習得している必要がある
# Kは習得している必要がある技の個数

# 技Nを習得するために必要な最短時間は?
# 技Nの習得に必要な技を最短で習得する

# 技の習得の組み合わせがグラフになっていることを見抜くのが重要!!

Tn, Kn, An = TKA[n - 1][0], TKA[n - 1][1], TKA[n - 1][2:]

ans = 0
visited = [False] * n


def dfs(v):
    v -= 1
    global ans
    if visited[v]:
        return
    ans += TKA[v][0]
    visited[v] = True
    for e in TKA[v][2:]:
        dfs(e)

for A in An:
    dfs(A)
print(ans + Tn)
