import math
a, b, c, d = list(map(int, input().split()))

if c * d - b > 0:
    print(math.ceil(a / (c * d - b)))
else:
    print(-1)