x, y, z = list(map(int, input().split()))

_y = y / x

for i in range(10 ** 6 + 1):
    _z = i / z
    if _y > _z:
        ans = i
        
print(ans)