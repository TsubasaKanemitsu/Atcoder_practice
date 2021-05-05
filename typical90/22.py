# 45分
# 整数問題
# 最大公倍数

import math
a, b, c = list(map(int, input().split()))

abc = sorted([a, b, c])

_gcd = abc[0]
for i in range(1, 3):

    _gcd = math.gcd(_gcd, abc[i])

ans = 0
for i in range(3):
    ans += abc[i] // _gcd - 1
print(ans)

