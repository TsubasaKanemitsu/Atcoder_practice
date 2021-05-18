x, y, z = list(map(int, input().split()))

money = y / x
ans = 0
for i in range(10 ** 6 + 1):
    if money > i / z:
        ans = max(ans, i)
print(ans)