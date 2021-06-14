import math
a, b, x = list(map(int, input().split()))


x = x / a

if x > a * b / 2:
    print(math.degrees(math.atan2(2 * (a * b - x), a ** 2)))
else:
    print(math.degrees(math.atan2(b ** 2, 2 * x)))