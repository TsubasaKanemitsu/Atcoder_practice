l, r = list(map(int, input().split()))

ans = 10 ** 15
for i in range(l, min(l + 2020, r + 1)):
    for j in range(i + 1, min(l + 2020, r + 1)):
        ans = min(ans, (i * j) % 2019)
print(ans)
