S = list(input())
mod = (10 ** 9 + 7)
dp = [[0] * 9 for _ in range(len(S) + 1)]
dp[0][0] = 1

for i in range(len(S)):
    for j in range(9):
        # print(i, j)
        # print(S[i])
        # 文字を選ばない場合
        dp[i + 1][j] += dp[i][j]
        # 文字を選ぶ場合
        if S[i] == 'c' and j == 0:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if S[i] == 'h' and j == 1:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if S[i] == 'o' and j == 2:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if S[i] == 'k' and j == 3:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if S[i] == 'u' and j == 4:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if S[i] == 'd' and j == 5:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if S[i] == 'a' and j == 6:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if S[i] == 'i' and j == 7:
            dp[i + 1][j + 1] += dp[i][j] % mod
    for j in range(8):
        dp[i + 1][j] %= mod
print(dp[len(S)][8] % mod)
