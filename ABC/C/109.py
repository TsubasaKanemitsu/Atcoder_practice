# 8分半
import math

n, X = list(map(int, input().split()))
x_list = list(map(int, input().split()))

min_val = min(x_list)

diff = []
for x in x_list:
    _diff = abs(X - x)
    if _diff == 0:
        _diff = 2
    diff.append(_diff)
# print(diff)

gcd = diff[0]
for i in range(1, len(diff)):
    gcd = math.gcd(gcd, diff[i])

print(gcd)