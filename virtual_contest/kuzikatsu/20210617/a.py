a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

ans = - 10 ** 10
for x in [a, b]:
    for y in [c, d]:
        ans = max(ans, x - y)
print(ans)