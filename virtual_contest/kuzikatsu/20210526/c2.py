n = int(input())

def divisor(n):
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if n // i != i:
                res.append(n // i)
        i += 1
    return res

cnt = 0
for i in range(1, n + 1):
    if len(divisor(i)) == 8 and i % 2 == 1:
        cnt += 1
print(cnt)