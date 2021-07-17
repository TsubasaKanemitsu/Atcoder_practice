from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]
# 0 -> +, 1 -> -
dp[0][0] = A[0]
dp[0][1] = A[0]

for i in range(1, n):
    dp[i][0] += dp[i - 1][0] + dp[i - 1][1] + A[i] + A[i]
    dp[i][1] += dp[i - 1][0] - A[i]
    print(dp)
print(sum(dp[n - 1]) % (10 ** 9 + 7))
