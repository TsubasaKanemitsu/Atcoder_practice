n = int(input())
ans = 10 ** 99
for b in range(61):
    ii = pow(2, b)
    a = n // ii
    c = n - ii * a
    if c >= 0:
        ans = min(ans, a + b + c)
print(ans)