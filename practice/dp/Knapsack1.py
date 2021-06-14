N, W = list(map(int, input().split()))
WV = [list(map(int, input().split())) for _ in range(N)]


value = [[0] * (W + 1) for _ in range(N)]
value[0][0] = 0

for i in range(N):
    wi, vi = WV[i]
    for w in range(W + 1):
        # 品物iを使わない場合
        value[i][w] = max(value[i][w], value[i - 1][w])
        
        # 品物iを使う場合
        if w - wi >= 0:
            value[i][w] = max(value[i][w], value[i - 1][w - wi] + vi)
print(value[N - 1][W])
