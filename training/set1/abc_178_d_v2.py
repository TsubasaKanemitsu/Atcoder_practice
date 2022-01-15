# https://atcoder.jp/contests/abc178/editorial/2430
# 復習
s = int(input())
# 数列の個数をkとすると、
# k = 1, 2, 3, ..., s // 3となる
# (各数列は3以上であるため)
# このとき、仕切りの数は0, 1, 2, ..., s // 3 - 1
# すなわち仕切りの数はk - 1個となる

# 数列の組み合わせを考えるためには,
# 各数列に3を割り振った上で、残りの数をどこの数列に割り振るかを
# 考えればいい
# ということは、まずはs - 3kで各数列に3を割り振る分のだけ全体から引く
# 残りの数と仕切りの数の組み合わせを考えることで
# 3以上を確保したうえで、残りの数の割り振り方に関して組み合わせを考えることができる。

# s = 7とする
# ex. k = 1
# 仕切りは0
# 数列の組み合わせは以下の状態になる
# ooooooo

# ex. k = 2
# 仕切りの数は1
# ooooooo|
# この状態で3以上を確保すると
# oooooo, o|と分けることができる
# s - 3kでoが1つ残ることがわかる
# 仕切りの数は1なので
# o|の2つの要素の組み合わせを考えればいいことになる
# o|, |o

# 数式
# k = 1, 2, 3, ..., s // 3

# s // 3
# Σ s-2k - 1 C k - 1
# k = 1

# k = 1 ~ s // 3までの
# 組み合わせの総和で求めることができる

# 二項係数の高速計算
# n C k = n! // (k! * (n - k)!)より
# 階乗と階乗の逆元を累積積により
# 高速に求める必要がある
# 逆元の求め方を理解する必要がある


# O(N)
def binomial_coefficient_table(n):
    MOD = 10 ** 9 + 7
    fac = [0] * (n + 1)
    finv = [0] * (n + 1)
    inv = [0] * (n + 1)

    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1

    for i in range(2, n + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    return fac, finv


# O(1)
def binomial_coefficient(n, k, fac, finv):
    MOD = 10 ** 9 + 7
    if k < 0 or n < k:
        return 0
    k = min(k, n - k)
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


nn = s // 3
fac, finv = binomial_coefficient_table(s)
ans = 0
MOD = 10 ** 9 + 7
for k in range(1, nn + 1):
    a = s - 2 * k - 1
    b = k - 1
    # print(a, b)
    add = binomial_coefficient(a, b, fac, finv)
    ans += add % MOD
print(ans % MOD)