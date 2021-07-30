import math
a, b, x = list(map(int, input().split()))
x /= a
if x <= a * b / 2:
    h = 2 * x
    theta = math.atan2(b * b, h)
else:
    h = 2 * (a * b - x)
    theta = math.atan2(h, a * a)
ans = math.degrees(theta)
print(ans)