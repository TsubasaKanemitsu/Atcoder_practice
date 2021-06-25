n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

dp = [10 ** 99] * n
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, n):
    # あるK個前の足場から足場iまでこれる通り数の
    # 全ての掛かるコストのパターンを試し
    # もっともコストのかからないパターンを採用する
    j = 0
    while i - j >= 1 and j < k:
        dp[i] = min(dp[i], dp[i - (j + 1)] + abs(h[i] - h[i - (j + 1)]))
        j += 1
print(dp[n - 1])