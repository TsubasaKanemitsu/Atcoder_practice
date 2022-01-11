s = int(input())

com = [[0] * s for _ in range(s)]
com[0][0] = 1

n = s // 3

ans = 0
for i in range(1, s):
    com[i][0] = 1
    for j in range(1, i + 1):
        com[i][j] = com[i - 1][j - 1] + com[i - 1][j]
MOD = 10 ** 9 + 7
for k in range(1, n + 1):
    ans += com[s - 2 * k - 1][k - 1] % MOD
print(ans % MOD)