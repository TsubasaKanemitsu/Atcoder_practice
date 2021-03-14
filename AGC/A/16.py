import math
from collections import Counter
s = input()

s_cnt = Counter(s)

key = ''
ans = 10 ** 99
for k, v in s_cnt.items():
    num = v
    cnt = 0
    n = len(s)
    for i in range(1, n):
        if s[i - 1] != k and s[i] == k:
            s[i - 1] = k
            cnt += 1

    ans = min(ans, cnt)
print(ans)