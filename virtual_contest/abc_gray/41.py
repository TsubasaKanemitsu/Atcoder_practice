# ABC 185C
# 組み合わせ

import math
L = int(input())

ans = math.factorial(L - 1) // (math.factorial(L - 12) * math.factorial(11))
print(ans)