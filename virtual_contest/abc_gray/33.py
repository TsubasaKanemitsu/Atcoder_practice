# ABC 168 C
# 20min ?
# 三角関数 苦手
import math
a, b, h, m = list(map(int, input().split()))

min_ = h * 60 + m

theta_a = min_ / 720 * 360 % 360
theta_b = min_ / 60 * 360 % 360

x1 = a * math.cos(math.radians(theta_a))
y1 = a * math.sin(math.radians(theta_a))

x2 = b * math.cos(math.radians(theta_b))
y2 = b * math.sin(math.radians(theta_b))

ans = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(ans)