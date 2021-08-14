n, m = list(map(int, input().split()))

ans = 0

if m >= 2 * n:
    ans = n + (m - 2 * n) // 4
else:
    ans = m // 2
print(ans)