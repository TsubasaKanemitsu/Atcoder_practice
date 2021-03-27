import math
n = int(input())
a = list(map(int, input().split()))

_gcd = a[0]
for i in range(1, n):
    _gcd = math.gcd(_gcd, a[i])
print(_gcd)