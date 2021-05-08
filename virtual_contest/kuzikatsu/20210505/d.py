n = int(input())

def divisor(n):
    result = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
        i += 1
    return result

div = divisor(n)
ans = 0
for d in div:
    if d == 1:
        continue
    if n // (d - 1) == n % (d - 1):
        ans += (d - 1)
print(ans)