a, b = list(map(int, input().split()))
b += 1
c, d = list(map(int, input().split()))
d += 1

ans = - 100 ** 100

for x in range(a, b):
    for y in range(c, d):
        ans = max(ans, x - y)
print(ans)