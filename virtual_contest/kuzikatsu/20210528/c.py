import math
r, x, y = list(map(int, input().split()))

D = math.sqrt(x ** 2 + y ** 2)

if D < r:
    print(2)
elif D == r:
    print(1)
else:
    print(math.ceil(D / r))