import math
h = int(input())
w = int(input())
n = int(input())

cnt = 0

if w >= h:
    cnt += math.ceil(n / w)
else:
    cnt += math.ceil(n / h)
print(cnt)