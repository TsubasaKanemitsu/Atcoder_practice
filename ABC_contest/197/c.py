n = int(input())

a = list(map(int, input().split()))

ans = 10 ** 100

for bit in range(1 << n):
    xored = 0
    ored = 0
    for j in range(n):
        if j < n:
            ored = ored | a[j]
        if j == (n - 1) or bit & (1 << j):
            xored ^= ored
            ored = 0
    ans = min(ans, xored)
print(ans)
