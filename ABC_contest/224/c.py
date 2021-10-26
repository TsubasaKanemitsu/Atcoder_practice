import math
n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]



ans = 0
for i in range(n):
    x1, y1 = XY[i]
    for j in range(i + 1, n):
        x2, y2 = XY[j]
        for k in range(j + 1, n):
            ans += 1
            x3, y3 = XY[k]
            # if i == 0 and j == 1 and k == 3:
            dx1 = abs(x1 - x2)
            dy1 = abs(y1 - y2)
            dx2 = abs(x1 - x3)
            dy2 = abs(y1 - y3)
            dx3 = abs(x2 - x3)
            dy3 = abs(y2 - y3)
            if dx1 == 0 and dx2 == 0 and dx3 == 0:
                ans -= 1
            if dx1 > 0 and dx2 > 0 and dx3 > 0:
                if (dy1 / dx1) == (dy2 / dx2) == (dy3 / dx3):
                    ans -= 1

            
print(ans)
