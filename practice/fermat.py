mod = 13


def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


def modinv(a, mod):
    return modpow(a, mod - 2, mod)

# fermatの小定理
def modinv2(a, mod):
    return pow(a, mod - 2, mod)


for i in range(1, 13):
    print(i, ":", modinv2(i, 13))
