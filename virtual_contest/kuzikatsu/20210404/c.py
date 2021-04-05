n = int(input())
X = list(map(int, input().split()))

def factorization(n):
    i = 2
    data = []
    while i * i <= n:
        if n % i == 0:
            ex = 0
            while n % i == 0:
                n /= i
                ex += 1
            data.append([i, ex])
        i += 1

    if n != 1:
        data.append([n, 1])
        
    return data


data = []
for x in X:
    d = factorization(x)
    data.append(d[0][0])

prime = list(set(data))

ans = 1
for p in prime:
    ans *= p
print(ans)