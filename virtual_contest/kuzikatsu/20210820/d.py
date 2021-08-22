# Atcoder Petrozavodsk Contest 001
# https://atcoder.jp/contests/apc001/submissions/me

# 考察
# AとBは1操作で1ずつ差が縮まるので、操作回数はBとAの総和の差であるsum(B) - sum(A)となる
# ai > bi のとき、biをai - bi回、1増やす必要がある
# ai < bi のとき、aiを(bi - ai) // 2回、2増やす必要がある
# この2つの式で必要最低限の1加算、2加算を計算し、それが操作回数より多くなければ答えはYES
# 操作回数を超えればNO

# 解説AC
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    if b[i] > a[i]:
        ans += (b[i] - a[i]) // 2
    elif a[i] > b[i]:
        ans -= a[i] - b[i]

if ans >= 0:
    print("Yes")
else:
    print("No")
