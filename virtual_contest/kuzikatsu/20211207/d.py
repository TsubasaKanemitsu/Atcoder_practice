n, a, b = list(map(int, input().split()))

# 答えとなる数式は
# 2 ^ n - (nCa + nCb + 1)
MOD = 10 ** 9 + 7
pow_ = pow(2, n, MOD)

# 繰り返し二乗法
# 二項係数の高速化

N = min(n, 2 * 10 ** 5)
fact = [1, 1] # fact[n] = (n! mod p)
factinv = [1, 1] # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1] # fact inv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

com = [0] * (N + 1)
com[0] = 1
for i in range(1, N + 1):
    com[i] = (com[i - 1] * ((n - i + 1) * inv[i] % MOD)) % MOD


def cmb(r):
    return com[r]

ans = (pow_ - (cmb(a) + cmb(b) + 1) % MOD) % MOD
print(ans)