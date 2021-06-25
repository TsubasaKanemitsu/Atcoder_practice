# 17分
# GCD, 素因数分解

n, p = list(map(int, input().split()))

def factorization(n):
    if n == 1:
        return [(1, 1)]

    i = 2
    result = []
    while i * i <= n:
        if n % i == 0:
            e = 0
            while n % i == 0:
                n = n // i
                e += 1
            result.append((i, e))
        i += 1

    if n != 1:
        result.append((n, 1))
    
    return result


result = factorization(p)
ans = 1

for i in range(len(result)):
    num, cnt = result[i]
    ans *= num ** (cnt // n)

print(ans)