# 解説
# https://drken1215.hatenablog.com/entry/2020/05/18/174000

# BFS & 累積和
# DFSを利用して頂点から子の累積和を求める

from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

n, q = list(map(int, input().split()))

tree = defaultdict(list)

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

val = defaultdict(int)

for i in range(q):
    p, x = list(map(int, input().split()))
    val[p] += x

res = [0] * (n + 1)

visited = defaultdict(lambda: False)

def dfs(v):
    visited[v] = True
    res[v] += val[v]
    for e in tree[v]:
        if not visited[e]:
            res[e] += res[v]
            dfs(e)

dfs(1)

for i in range(1, n + 1):
    print(res[i], end=" ")
print()