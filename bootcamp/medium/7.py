# 10分30秒
from collections import Counter
n = int(input())
s = input()

cnt1 = Counter(s)
cnt2 = Counter()

for k, v in cnt1.items():
    cnt2[k] = 0

ans = 0
for ss in s:
    cnt1[ss] -= 1
    cnt2[ss] += 1
    cnt = 0
    for k in cnt1.keys():
        if cnt1[k] > 0 and cnt2[k] > 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)