n = int(input())
s = list(input())

dp = [[0] * 8 for _ in range(n + 1)]
mod = (10 ** 9 + 7)
ans = "atcoder"
dp[0][0] = 1

for i in range(n):
    for j in range(8):
        # 文字選ばない場合
        dp[i + 1][j] += dp[i][j]
        
        # 文字を選ぶ場合
        if s[i] == 'a' and j == 0:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if s[i] == 't' and j == 1:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if s[i] == 'c' and j == 2:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if s[i] == 'o' and j == 3:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if s[i] == 'd' and j == 4:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if s[i] == 'e' and j == 5:
            dp[i + 1][j + 1] += dp[i][j] % mod
        if s[i] == 'r' and j == 6:
            dp[i + 1][j + 1] += dp[i][j] % mod
            
    for j in range(8):
        dp[i + 1][j] %= mod
print(dp[n][7] % mod)
