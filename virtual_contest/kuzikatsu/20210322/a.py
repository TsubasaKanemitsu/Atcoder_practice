n = int(input())

if n % 1000 == 0:
    ans = 1000 * (n // 1000)
else:
    ans = 1000 * (n // 1000 + 1)
print(ans - n)