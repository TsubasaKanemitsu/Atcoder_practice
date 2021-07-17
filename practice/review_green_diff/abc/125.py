n = int(input())
A = list(map(int, input().split()))

dp = [[-10 ** 10] * 2 for _ in range(n + 1)]
dp[0][0] = 0

# 反転させたときとさせないときでi番目までに大きくなる値を更新し続ける
for i in range(n):
    # 前の段階で、反転していたかどうかで足す値に-1を掛けるかを決める
    dp[i + 1][0] = max(dp[i][0] + A[i], dp[i][1] - A[i])
    dp[i + 1][1] = max(dp[i][0] - A[i], dp[i][1] + A[i])
print(dp[n][0])