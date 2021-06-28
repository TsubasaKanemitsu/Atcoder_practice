# 最長共通部分列問題
# 二種類の文字列の番号を状態として持つ
# Sのi番目とTのi番目の状態がどうであるか

s = list(input())
t = list(input())

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

for i in range(len(s)):
    for j in range(len(t)):
        # Sのi番目とTのj番目が同じとき，共通部分列の長さは1つ増える
        
        # 文字が共通であるとき
        if s[i] == t[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        # 文字が共通でないとき
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])

ans = ''

i = len(s)
j = len(t)

while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        # 共通文字列の長さが1つ前の状態と異なるということは
        # 現在のi, j番目の組み合わせの状態で共通部分文字列が存在していたということ
        # よってs[i - 1] = t[j - 1]より(後ろの文字列から追加するので)
        ans = s[i - 1] + ans
        i -= 1
        j -= 1
print(ans)