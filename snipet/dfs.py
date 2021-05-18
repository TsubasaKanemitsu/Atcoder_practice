from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
E = defaultdict(list)
# 隣接リストの作成
for i in range(n):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)


# 頂点に訪れたかどうかを判定
visited = [False] * n 


# 再帰関数のdfs
def dfs(v):
    visited[v] = True
    for i in E[i]:
        # 頂点に未訪問であればdfsを呼び出す
        if not visited[i]:
            dfs(i)