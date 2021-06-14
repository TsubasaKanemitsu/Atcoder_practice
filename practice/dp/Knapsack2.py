# 重さと価値の初期化をミスした
n, w = list(map(int, input().split()))

WV = [[0, 0]]
sum_val = 0
sum_weight = 0
for i in range(n):
    ww, vv = list(map(int, input().split()))
    WV.append([ww, vv])
    sum_weight += ww
    sum_val += vv

# 最大ケースで価値の総和が取り得る値は10 ** 5
weight = [[sum_weight] * (sum_val + 1) for _ in range(n + 1)]
weight[0][0] = 0

for i in range(1, n + 1):
    wi, vi = WV[i]
    
    for v in range(sum_val + 1):
        # i個目の荷物を入れない場合
        weight[i][v] = min(weight[i][v], weight[i - 1][v])
        
        # i個目の荷物を入れる場合
        if v - vi >= 0 and weight[i - 1][v - vi] + wi <= w:
            weight[i][v] = min(weight[i][v], weight[i - 1][v - vi] + wi)

ans = 0
for i in range(n + 1):
    for v in range(sum_val + 1):
        if weight[i][v] <= w:
            ans = max(ans, v)
print(ans)