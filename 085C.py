N, Y = list(map(int, input().split()))

res_x = -1
res_y = -1
res_z = -1
for x in range(0, N + 1):
    for y in range(0, N - x + 1):
        z = N - x - y
        total = 10000 * x + 5000 * y + 1000 * z
        if total == Y:
            res_x = x
            res_y = y
            res_z = z

print(res_x, res_y, res_z)
