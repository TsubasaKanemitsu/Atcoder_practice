import math

x, y = list(map(int, input().split()))

diff = y - x
if diff <= 0:
    print(0)
else:
    print(math.ceil(diff / 10))