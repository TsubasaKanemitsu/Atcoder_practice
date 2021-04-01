# https://img.atcoder.jp/arc067/editorial.pdf

# 方針
# N!を求めて，愚直に約数を列挙するのは計算量的に不可能
# 約数の個数は，素因数分解した全ての約数の累乗数を掛けることで
# 求めることができる性質を利用する．
# N!は1 ~ Nまでを掛け算した値なので，各値に対して素因数分解を行い，
# 素因数の累乗数を求めていく
# 求まった全ての素因数の(累乗数 + 1)を掛けていくことでN!の約数の個数が求まる

from collections import defaultdict
n = int(input())

def factorization(n):
    i = 2
    result = []
    while i * i <= n:
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n = n // i
            result.append((i, ex))
        i += 1

    if n != 1:
        result.append((n, 1))
    
    return result

ex = defaultdict(int)

ans = 1
for i in range(1, n + 1):
    for f in factorization(i):
        ex[f[0]] += f[1]

ans = 1
for k, v in ex.items():
    ans *= (v + 1)
print(ans % (10 ** 9 + 7))

