r, g, b, n = list(map(int, input().split()))

cnt = 0
for i in range(n // r + 1):
    for j in range(n // g + 1):
        hako = n - r * i - g * j
        k = hako / b
        if k >= 0 and k.is_integer() and r * i + g * j + k * b == n:
            cnt += 1
print(cnt)