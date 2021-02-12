# 6分
# 1WA
from collections import defaultdict
n, m = list(map(int, input().split()))

flag = defaultdict(bool)
wa = defaultdict(int)
ac = 0
_wa = 0
for _ in range(m):
    p, s = list(input().split())
    p = int(p)
    if not flag[p] and s == 'WA':
        wa[p] += 1
    elif not flag[p] and s == 'AC':
        ac += 1
        flag[p] = True
        _wa += wa[p]
print(ac, _wa)