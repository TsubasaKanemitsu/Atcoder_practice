# ABC 148
# 1分30秒

# 最小公倍数

import math
a, b = list(map(int, input().split()))

ans =  a * b // math.gcd(a, b)
print(ans)