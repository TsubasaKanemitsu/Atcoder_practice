N, K = list(map(int, input().split()))

dp = [[0] * (K + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    for j in range(K):
        # K回未満連続コインが裏になる確率を計算
        # 連続
        if j + 1 < K:
            dp[i + 1][j + 1] += dp[i][j] / 2
        # i + 1回目の試行を裏が出た1回目とみなす
        # 連続では無くなった
        dp[i + 1][1] += dp[i][j] / 2
        

sm = 0
for i in range(K):
    sm += dp[N][i]
print(1 - sm)