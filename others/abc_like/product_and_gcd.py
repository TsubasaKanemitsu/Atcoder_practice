import math
n, p = list(map(int, input().split()))

def factorization(n):
    i = 2
    result = []

    while i * i <= n:
        if n % i == 0:
            ex = 0
            while n % i == 0:
                n = n // i
                ex += 1
            result.append([i, ex])
        i += 1
    if n != 1:
        result.append([n, 1])
    else:
        result.append([1, 1])

    print(result)

    return result


X = factorization(p)
print(X)
num = X[0][0] ** X[0][1]
print(num)
for i in range(1, len(X)):
    num = math.gcd(num, X[i][0] ** X[i][1])

print(num)