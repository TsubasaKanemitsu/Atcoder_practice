x, y = list(map(int, input().split()))

x, y = sorted([x, y], reverse=True)

dist = x + y

if dist % 3 != 0:
    print(0)
    exit()

total = int(x + y) // 3
n = x - total
m = y - total

if n < 0 or m < 0:
    print(0)
    exit()


def make_tables(n):
    mod = 10 ** 9 + 7
    fac = [1, 1]
    ifac = [1, 1]
    inv = [0, 1]

    for i in range(2, n + 1):
        fac.append(fac[i - 1] * i % mod)
        inv.append(-(mod // i) * inv[mod % i] % mod)
        ifac.append(ifac[i - 1] * inv[-1] % mod)

    return fac, ifac

def comb(n, k):
    
    mod = 10 ** 9 + 7
    fac, ifac = make_tables(n)

    return fac[n] * ifac[k] * ifac[n - k] % mod

ans = comb(total, n)
print(ans)