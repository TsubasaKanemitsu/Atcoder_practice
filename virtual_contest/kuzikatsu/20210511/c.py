from collections import defaultdict
import itertools
n, m = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
CD = [list(map(int, input().split())) for _ in range(k)]

ans = 0
for prod in itertools.product([0, 1], repeat=k):
    cnt = defaultdict(int)
    for i in range(k):
        num = CD[i][prod[i]]
        cnt[num] += 1
    temp_cnt = 0
    for j in range(m):
        a, b = AB[j]
        if cnt[a] >= 1 and cnt[b] >= 1:
            temp_cnt += 1
    ans = max(ans, temp_cnt)
print(ans)