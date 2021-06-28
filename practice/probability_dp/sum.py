n, K = list(map(int, input().split()))

dp = [[0] * (K + 1) for _ in range(n + 1)]

dp[0][0] = 1

for i in range(n):
    for j in range(K + 1):
        for k in range(1, 7):
            dp[i + 1][min(K, j + k)] += dp[i][j] / 6
print(dp[n][K])
