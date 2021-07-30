n, k = list(map(int, input().split()))

if n == 1 and k != 1:
    print(k)
    exit()
elif n == 1 and k == 1:
    print(1)
    exit()
mod = 10 ** 9 + 7

ans = k % mod * (k - 1) % mod
ans = ans * pow(k - 2, n - 2, mod) % mod
print(ans)