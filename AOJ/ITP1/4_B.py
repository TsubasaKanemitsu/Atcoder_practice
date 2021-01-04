import math

r = float(input())
pi = math.pi

area = round(pi * (r ** 2), 6)
lap = round(2 * pi * r, 6)

print(area, lap)