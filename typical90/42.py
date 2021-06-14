import sys
sys.setrecursionlimit(10 ** 7)
k = int(input())

# 9の倍数は数字の和が9の倍数となる．
# 各数字の和であるKが9の倍数であれば，Xは9の倍数である．

if k % 9 != 0:
    print(0)
    exit()
else:
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1, k + 1):
        add = min(i, 9)
        for j in range(1, add + 1):
            dp[i] += dp[i - j]
print(dp[k] % (10 ** 9 + 7))