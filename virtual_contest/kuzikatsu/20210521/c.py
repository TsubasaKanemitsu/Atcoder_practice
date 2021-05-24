q, h, s, d = list(map(int, input().split()))
n = int(input())

if n % 2 == 0:
    ans = n // 2 * min(q * 8, h * 4, 2 * s, d)
else:
    ans = n // 2 * min(q * 8, h * 4, 2 * s, d)
    ans += min(q * 4, h * 2, s)
print(ans)