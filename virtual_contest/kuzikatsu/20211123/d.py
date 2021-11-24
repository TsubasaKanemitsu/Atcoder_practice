# 二項係数を求めるDP

A, B, K = list(map(int, input().split()))

# AとBで作ることができる文字列の組み合わせはa+bCaである
# 先頭がaから始まるかbから始まるかは、組み合わせ数がKより大きい場合はB、Kより小さい場合はAとなる。

dp = [[0] * (B + 1) for _ in range(A + 1)]

dp[0][0] = 1

for i in range(A + 1):
    for j in range(B + 1):
        
        if 0 <= j - 1:
            dp[i][j] += dp[i][j - 1]
        if 0 <= i - 1:
            dp[i][j] += dp[i - 1][j]
# print(dp)
n = A + B

ans = ''
for i in range(n):
    if A > 0:
        # Aから始まる文字列の組み合わせが何個あるかを考えるのでA - 1
        if K <= dp[A - 1][B]:
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            # Aから始まる文字列を省いた上での順位を知る必要があるため
            K -= dp[A - 1][B]
            B -= 1
    else:
        ans += 'b'
        B -= 1
print(ans)