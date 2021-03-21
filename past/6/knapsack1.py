n, w = list(map(int, input().split()))

# 1始まりにするために先頭にダミーを入れる
ws = [0]
vs = [0]

for i in range(n):
    ww, v = list(map(int, input().split()))
    ws.append(ww)
    vs.append(v)

# value[i][w]: 品物iまで見て重さ合計wであるときの価値の総和の最大値
# 非常に小さい値で初期化しておく
value = []
for i in range(n + 1):
    value.append([-10 ** 18] * (w + 1))

# 初期条件
value[0][0] = 0

# iが小さい順に求めていく
for i in range(1, n + 1):
    for ww in range(w + 1):
        # 品物iを使わない場合
        value[i][ww] = max(value[i][ww], value[i - 1][ww])
        # 品物iを使う場合
        if ww - ws[i] >= 0:
            value[i][ww] = max(value[i][ww], value[i - 1][ww - ws[i]] + vs[i])
# value[n][0], ..., value[n][w]の中で一番価値の総和が大きいものを答えとする
ans = max(value[n])
print(ans)