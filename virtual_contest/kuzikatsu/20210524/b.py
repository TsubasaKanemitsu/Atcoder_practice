x, y, z = list(map(int, input().split()))

cnt = x // (y + z)
x -= cnt * (y + z) + z
if x >= 0:
    print(cnt)
else:
    print(cnt - 1)
