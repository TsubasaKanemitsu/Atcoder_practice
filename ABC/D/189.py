# import itertools
n = int(input())
S = [input() for _ in range(n)]

# 愚直解
# cnt = 0
# for perm in itertools.product([True, False], repeat=(n + 1)):
#     ans = perm[0]
#     for i in range(n):
#         if S[i] == 'AND':
#             ans &= perm[i + 1]
#         elif S[i] == 'OR':
#             ans |= perm[i + 1]
#     if ans:
#         cnt += 1
# print(cnt)

# https://atcoder.jp/contests/abc189/editorial/537
# n = 1のとき，y_n = Trueの1通り
# True, Falseとなるときの条件を考える
# X_n, Y_n-1の関係性
# 漸化式

ans = 1
for i in range(n - 1, -1, -1):
    if S[i] == 'OR':
        ans += 2 ** (i + 1)
print(ans)