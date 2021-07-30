# ABC 162 C
# 1分
# 複数項の最大公約数

import math
k = int(input())

ans = 0

for i in range(1, k + 1):
    for j in range(1, k + 1):
        for kk in range(1, k + 1):
            ans += math.gcd(math.gcd(i, j), kk)
print(ans)