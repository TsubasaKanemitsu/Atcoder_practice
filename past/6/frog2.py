n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

dp = [10 ** 99 + 1] * (n + 1)

dp[0] = 0
# dp[1] = h[1] - h[0]

for i in range(1, n):
    dp[i] = dp[i - 1] + abs(h[i - 1] - h[i])
    
    for j in range(1, k + 1):
        # j番目前からi番目までの経路で一番最小のコストでi番目に到達できる経路を探索
        if i >= j:
            dp[i] = min(dp[i], dp[i - j] + abs(h[i - j] - h[i]))
print(dp[n - 1])