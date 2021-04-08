# 9分

from collections import Counter, defaultdict
n = int(input())

A = list(map(int, input().split()))
a_cnt = Counter(A)

ans = 0
for k in a_cnt.keys():
    sm = a_cnt[k - 1] + a_cnt[k] + a_cnt[k + 1]
    ans = max(sm, ans)

print(ans)