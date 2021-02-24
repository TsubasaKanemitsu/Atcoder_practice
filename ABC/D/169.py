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

if n == 1:
    print(0)
    exit()

soinsuu = factorization(n)
# print(soinsuu)
cnt = 0
for s in soinsuu:
    e = 1
    ex = s[1]
    while ex >= e:
        ex -= e
        e += 1
        cnt += 1
print(cnt)
