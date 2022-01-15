# 15分
import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict
from re import X
n, q = list(map(int, input().split()))

tree = defaultdict(list)
cnt = defaultdict(int)

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

for _ in range(q):
    p, x = list(map(int, input().split()))
    p -= 1
    cnt[p] += x

visited = [False] * n
ans = [0] * n

def dfs(v, cnt_val):
    if visited[v]:
        return

    visited[v] = True
    cnt_val += cnt[v]
    ans[v] = cnt_val
    for e in tree[v]:
        if not visited[e]:
            dfs(e, cnt_val)
    cnt_val -= cnt[v]

dfs(0, 0)

print(*ans)