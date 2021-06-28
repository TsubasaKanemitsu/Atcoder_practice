import math
a, b, c, d = list(map(int, input().split()))

if c * d - b > 0:
    ans = math.ceil(a / (c * d - b))
    print(ans)
else:
    print(-1)