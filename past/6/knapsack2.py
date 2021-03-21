# 価値の総和の制約が10 ** 3乗なので，価値の総和の状態を変更しつつ
# 重さw以下での価値の最大化を目指す
N, W = list(map(int, input().split()))

ws = [0]
vs = [0]
for i in range(N):
    w, v = list(map(int, input().split()))
    ws.append(w)
    vs.append(v)

# 価値の最大値(重さ無視)
# DP時には，W以下の場合だけ値を探索するようにすればいい
max_v = sum(vs) + 1

weight = []
for i in range(N + 1):
    weight.append([10 ** 18] * (max_v))

weight[0][0] = 0

for i in range(1, N + 1):
    for v in range(max_v):
        # i番目の荷物を選ばない
        weight[i][v] = min(weight[i][v], weight[i - 1][v])
        
        # 価値vを入れるのに必要な最小の重量を求める
        if v - vs[i] >= 0:
            weight[i][v] = min(weight[i][v], weight[i - 1][v - vs[i]] + ws[i])
        

for i in range(max_v - 1, -1, -1):
    if weight[N][i] <= W:
        ans = i
        break
print(ans)