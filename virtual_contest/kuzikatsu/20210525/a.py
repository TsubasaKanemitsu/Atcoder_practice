import math
xa, ya, xb, yb, xc, yc = list(map(int, input().split()))

ac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
bc = ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5

cos_theta = (ac ** 2 + ab ** 2 - bc ** 2) / (2 * ab * ac)
sin_theta = math.sqrt(1 - cos_theta ** 2)

s = 0.5 * ab * ac * sin_theta
print(s)