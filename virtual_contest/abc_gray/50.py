# ABC 200 C
# mod
# 5min

# Ai - Ajは200の倍数であるということは、200で割った余りが同じになっている数のうち
# 2つ選ぶ組み合わせの数を求めればいい

# 200の倍数 == 200で割ったときの余りが同じ

import math
from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

mod = 200


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

B = defaultdict(int)
for i in range(n):
    B[A[i] % 200] += 1

ans = 0
for k, v in B.items():
    if v >= 2:
        ans += combinations_count(v, 2)
print(ans)