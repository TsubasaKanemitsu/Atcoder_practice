n = int(input())

# 状態: お金
# 値: 操作回数
dp = [10 ** 9] * (n + 1)
dp[0] = 0

for i in range(n + 1):
    x = 0
    y = 0
    # 9の累乗
    while n >= i + 9 ** (x + 1):
        x += 1
        dp[i + 9 ** x] = min(dp[i] + 1, dp[i + 9 ** x])
    
    # 6の累乗
    while n >= i + 6 ** (y + 1):
        y += 1
        dp[i + 6 ** y] = min(dp[i] + 1, dp[i + 6 ** y])

    if i + 1 <= n:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

print(dp[n])