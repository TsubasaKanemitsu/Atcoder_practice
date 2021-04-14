import math
r, x, y = list(map(int, input().split()))

z = x ** 2 + y ** 2
dist = math.sqrt(z)
if dist == r:
    print(1)
elif dist <= 2 * r:
    print(2)
else:
    print(math.ceil(dist / r))