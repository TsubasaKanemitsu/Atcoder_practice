import math
# ABC D 136
# https://drken1215.hatenablog.com/entry/2020/12/29/190100
S = list(input())

# 考察
# RとLの境目では、移動する個数は変わらないので
# R側とL側で分割して考える
# R側とL側でどのように個数をカウントするのかがわからなかった

# 回答
# それぞれの境目に集まる子供の数は、最初にいる位置によって決まるので
# ○と×で考えてみる
# R R R R R R | L L L L L L
# x o x o x o | x o x o x o
# このように表すと、RとLにいる子供が最終的に集まる数が分かる

# 移動して子供が集まる位置を不変量として考える。

ans = [0] * len(S)

cnt = 0
for i in range(len(S)):
    if S[i] == 'R':
        cnt += 1
    else:
        ans[i] += cnt // 2
        ans[i - 1] += (cnt + 1) // 2
        cnt = 0

cnt = 0
for i in range(len(S) - 1, -1, -1):
    if S[i] == 'L':
        cnt += 1
    else:
        ans[i] += cnt // 2
        ans[i + 1] += (cnt + 1) // 2
        cnt = 0

print(*ans)


# RとLの境目に子供が集まることがわかる
# 境目に集まる子供の数え方を考える必要がある。
# 最終的にR側に集まる子供とL側に集まる子供の位置を
# oとxで表すことができる。
# その個数を数え上げていけば、RとLの境界値の値を
# 求めることができる。
