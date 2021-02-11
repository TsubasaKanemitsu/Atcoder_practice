from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

ans = 0
for a in set(A):
    if cnt[a] >= a:
        ans += cnt[a] - a
    else:
        ans += cnt[a]
print(ans)
