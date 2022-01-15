# 復習

s = int(input())

MOD = 10 ** 9 + 7

# dp = [[False] * (s + 1) for _ in range(700)]
# # 存在し得る値かどうか
# for i in range(3, s + 1):
#     dp[0][i] = True
# # 存在し得る値の数(項数は最大で 2000 // 3程度なので700にした)
# cnt = [[0] * (s + 1) for _ in range(700)]
# for i in range(3, s + 1):
#     cnt[0][i] = 1
# for i in range(1, 700):
#     for j in range(3, s + 1):
#         for k in range(3, s + 1):
#             if j + k <= s and dp[i - 1][j]:
#                 dp[i][j + k] = True
#                 cnt[i][j + k] += cnt[i - 1][j] % MOD
# ans = 0
# for i in range(700):
#     ans += cnt[i][s] % MOD

# print(ans)

# 実験で解く方法
dp = [0, 0, 0, 1]
for i in range(4, s + 1):
    dp.append((dp[-1] + dp[-3]) % MOD)
print(dp[s])
