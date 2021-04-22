n = int(input())

def factorization(n):
    result = []
    i = 2
    while i * i <= n:
        ex = 0
        while n % i == 0:
            n = n // i
            ex += 1
        result.append([i, ex])
        i += 1
    
    if n != 1:
        result.append([n, 1])
    return result


result = factorization(n)
ans = str(n) + ':'
for r in result:
    ans += (' ' + str(r[0])) * r[1]
print(ans)