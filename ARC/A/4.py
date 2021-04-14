import math
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        ans = max(ans, dist)
print(ans)