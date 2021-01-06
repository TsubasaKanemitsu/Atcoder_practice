Sx, Sy, Gx, Gy = list(map(int, input().split()))

x = float((Sy * Gx + Sx * Gy)) / float((Sy + Gy))

print(x)