# 深さ優先探索と見抜けてもう少しでACできそうだった．

from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

C = list(map(int, input().split()))
tree = defaultdict(list)

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * n
color_status = [0] * (10 ** 5 + 1)
ans = [False] * n

def dfs(v):
    visited[v] = True
    color_status[C[v]] += 1

    for e in tree[v]:
        if not visited[e]:
            if color_status[C[e]] == 0:
                ans[e] = True
            dfs(e)
    color_status[C[v]] -= 1
dfs(0)

for i in range(n):
    if i == 0:
        print(1)
    if ans[i]:
        print(i + 1)