n = int(input())


def factorization(n: int):
    i = 2
    res = []
    while i * i <= n:
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n = n // i
            res.append((i, ex))
        i += 1

    if n != 1:
        res.append((i, 1))

    return res


fact = factorization(n)

ans = 0
for prime, ex in fact:
    cnt = 1
    while ex - cnt >= 0:
        ex -= cnt
        cnt += 1
    ans += cnt - 1
print(ans)