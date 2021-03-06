# 10分
# 隣接リストを用いた実装

from collections import defaultdict
n, m, q = list(map(int, input().split()))

u = defaultdict(list)

# グラフの関係
for i in range(m):
    k, v = list(map(int, input().split()))
    # 無向グラフの場合は，始点と終点の関係を入れ替えた2パターンを隣接リストに書き込む
    u[k - 1].append(v - 1)
    u[v - 1].append(k - 1)

# 頂点の色
c = list(map(int, input().split()))

# クエリ
color = []
for _ in range(q):
    query = input().split()
    if len(query) == 2:
        x = int(query[1])
        color.append(c[x - 1])
        top = u[x - 1]
        for t in top:
            c[t] = c[x - 1]
    else:
        # 頂点
        x = int(query[1])
        color.append(c[x - 1])
        # 色
        y = int(query[2])
        c[x - 1] = y

for clr in color:
    print(clr)