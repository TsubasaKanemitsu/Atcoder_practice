# 1時間 4分
# DP
from collections import defaultdict
n, m = list(map(int, input().split()))
a = [int(input()) for _ in range(m)]

stairs = defaultdict(bool)
for i in range(m):
    stairs[a[i]] = True
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(1, n + 1):
    if i > 1:
        dp[i] = dp[i - 1] + dp[i - 2]
    if stairs[i]:
        dp[i] = 0
    
print(dp[n] % (10 ** 9 + 7))