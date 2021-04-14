import math
a, b, h, m = list(map(int, input().split()))

mnt = h * 60 + m
a_angle = 0.5 * mnt
b_angle = 6 * mnt

a_x = a * math.cos(math.radians(a_angle))
a_y = a * math.sin(math.radians(a_angle))

b_x = b * math.cos(math.radians(b_angle))
b_y = b * math.sin(math.radians(b_angle))

dist = math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)
print(dist)