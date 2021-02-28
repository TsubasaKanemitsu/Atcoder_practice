# 10分
from collections import defaultdict
n, m = list(map(int, input().split()))

wa_cnt = defaultdict(int)
ac_cnt = defaultdict(bool)
wa = 0
for i in range(m):
    p, s = list(input().split())
    p = int(p)
    if s == 'WA':
        wa_cnt[p] += 1
    else:
        if ac_cnt[p] == False:
            wa += wa_cnt[p]
        ac_cnt[p] = True
print(list(ac_cnt.values()).count(True), wa)
