n, a, x, y = list(map(int, input().split()))

ans = 0
if a <= n:
    ans += x * a
    ans += (n - a) * y
else:
    ans += x * n
print(ans)