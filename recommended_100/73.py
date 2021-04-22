import sys
sys.setrecursionlimit(10 ** 6)

x, y = list(map(int, input().split()))

x, y = sorted([x, y], reverse=True)

dist = x + y

if dist % 3 != 0:
    print(0)
    exit()

total = int(x + y) // 3
n = x - total
m = y - total
mod = 10 ** 9 + 7

if n < 0 or m < 0:
    print(0)
    exit()


def comb(n, k, mod, fac, ifac):
    k = min(k, n - k)
    return fac[n] * ifac[k] * ifac[n - k] % mod


def make_tables(mod, n):
    # 階乗テーブル
    fac = [1, 1]
    # 逆元の階乗テーブル
    ifac = [1, 1]
    # 逆元のテーブル
    inv = [0, 1]

    for i in range(2, n + 1):
        fac.append((fac[i - 1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i) % mod))
        ifac.append(ifac[i - 1] * inv[-1] % mod)

    return fac, ifac


fac, ifac = make_tables(mod, total)
ans = comb(total, n, mod, fac, ifac)
print(ans)