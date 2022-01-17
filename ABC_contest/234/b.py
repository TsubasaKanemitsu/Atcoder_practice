n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    x1, y1 = xy[i]
    for j in range(i + 1, n):
        x2, y2 = xy[j]
        dist = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
        ans = max(ans, dist)

print(ans)