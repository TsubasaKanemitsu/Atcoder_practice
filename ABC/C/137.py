# 18分
from collections import defaultdict
from math import factorial


def combinations_count(n, r):
    import math
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))

n = int(input())
S = [''.join(sorted(list(input()))) for _ in range(n)]

cnt = defaultdict(int)
for s in S:
    cnt[s] += 1
ans = 0
for k, v in cnt.items():
    if v >= 2:
        ans += combinations_count(v, 2)
print(ans)