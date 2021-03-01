from collections import Counter

def combinations_count(n, r):
    import math
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))


n = int(input())
S = [''.join(sorted(list(input()))) for _ in range(n)]

s_cnt = Counter(S)


ans = 0

for k, v in s_cnt.items():
    if v >= 2:
        ans += combinations_count(v, 2)
print(ans)