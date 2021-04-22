n = int(input())
a, b, c = list(map(int, input().split()))

ans = 10 ** 99
for i in range(9999 + 1):
    for j in range(9999 + 1 - i):
        diff = n - (a * i + b * j)
        k = diff // c
        mod = diff % c
        if diff < 0 or i + j + k > 9999 or mod != 0:
            continue
        ans = min(ans, i + j + k)
print(ans)