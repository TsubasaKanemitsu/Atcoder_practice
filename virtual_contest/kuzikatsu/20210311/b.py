sx, sy, gx, gy = list(map(int, input().split()))

x = sy * (gx - sx) / (gy + sy) + sx
print(x)