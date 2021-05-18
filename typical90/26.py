# 2部グラフは異なるグループに属する頂点同士が辺で結びついているかつ同じグループ同士が繋がっていない
# 状態のことを表す

# ABC126D

from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

V = defaultdict(list)
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    V[a].append(b)
    V[b].append(a)


# n個の頂点の色を初期化
colors = [0 for i in range(n)]


# 頂点vをcolor(1 or -1)で塗り，再帰的に矛盾がないか調べる．矛盾があればFalse
def dfs(v, color):
    colors[v] = color
    for to in V[v]:
        # 同じ色が隣接したらFalse
        if colors[to] == color:
            return False
        # 未着色の頂点があったら反転した色を指定し，再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False

    # 調べ終わったら矛盾がないのでTrue
    return True


dfs(0, 1)

flag = 0
for c in colors:
    flag += c

if flag >= 0:
    cnt = 0
    for i in range(n):
        if colors[i] == 1:
            cnt += 1
            print(i + 1, end=' ')
        if cnt == n // 2:
            break
else:
    cnt = 0
    for i in range(n):
        if colors[i] == -1:
            cnt += 1
            print(i + 1, end=' ')
        if cnt == n // 2:
            break
