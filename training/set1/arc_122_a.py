n = int(input())
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7
# dp
# 0 -> +, 1 -> -とする

dp = [[0] * 2 for _ in range(n)]
ans = [[0] * 2 for _ in range(n)]
# -が2回連続以上続かない式を列挙できる通り数
dp[0][0] = 1
# i番目までの総和
ans[0][0] = A[0]

for i in range(1, n):
    # 式に+を設定できるのは、ひとつ前が+と-のときなので
    # dp[i - 1][0]とdp[i - 1][1]の通り数を足す
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
    # 式に-を設定できるのは、ひとつ前が+のときなので
    # dp[i - 1][0]を足す
    dp[i][1] = dp[i - 1][0]
    # Aiまで良い式になっている場合のi番目までの総和
    ans[i][0] = (ans[i - 1][0] + ans[i - 1][1] + A[i] * dp[i][0]) % MOD
    ans[i][1] = (ans[i - 1][0] - A[i] * dp[i][1]) % MOD

print((ans[n - 1][0] + ans[n - 1][1]) % MOD)

# i番目に+, -を設定している式の本数の通り数を使用することでi + 1番目に加算を行う式の本数がわかる = 加算するAiの数がわかる
# i番目に-を設定している式の本数の通り数を使用することでi + 1番目に減産を行う式の本数がわかる = 減算するAiの数がわかる