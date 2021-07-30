# 10分
import math
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

time = 5
min_p = min(a, b, c, d, e)
n -= min_p
if n <= 0:
    print(time)
else:
    time += math.ceil(n / min_p)
    print(time)