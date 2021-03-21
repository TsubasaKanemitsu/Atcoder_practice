from collections import defaultdict
n, m = list(map(int, input().split()))

a = []
for _ in range(n):
    a.append(list(input()))

# 番号ごとに座標を分類

group = defaultdict(list)

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            nn = 0
        elif a[i][j] == 'G':
            nn = 10
        else:
            nn = int(a[i][j])
        group[nn].append([i, j])

# cost[i][j]: 数字を正しく通ってマス(i, j)にたどり着く最小移動回数
# 非常に大きい値で初期化しておく
cost = []
for i in range(n):
    cost.append([10 ** 100] * m)

# 初期条件 スタート地点の座標
si, sj = group[0][0]
cost[si][sj] = 0


# nが小さい方から順番に求めていく
for nn in range(1, 11):
    # 現在の番号の位置
    for i, j in group[nn]:
        # 1つ前の番号の位置
        for i2, j2 in group[nn - 1]:
            cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i - i2) + abs(j - j2))

# ゴール地点の座標はgroup[10][0]
# ただしゴール地点のcostがINFであれば，到達不可能なため-1を表示する
gi, gj = group[10][0]
ans = cost[gi][gj]
if ans == 10 ** 100:
    ans = -1
print(ans)
