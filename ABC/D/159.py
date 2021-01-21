# 54分
from collections import defaultdict
import itertools
import math
def combinations_count(n, r):
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))


n = int(input())
A = list(map(int, input().split()))

A_count = defaultdict(int)
for a in A:
    A_count[a] += 1

select_own = defaultdict(int)
select_other = defaultdict(int)
sum_other = 0

for key, value in dict(A_count).items():
    if value - 1 >= 2:
        select_own[key] = combinations_count(value - 1, 2)
    else:
        select_own[key] = 0
    
    if value >= 2:
        select_other[key] = combinations_count(value, 2)
    else:
        select_other[key] = 0
    sum_other += select_other[key]
    

ans = 0
for a in A:
    ans = 0
    
    ans = sum_other - select_other[a] + select_own[a]
    print(ans)