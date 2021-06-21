from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)

for a in A:
    cnt[a % 200] += 1

cnt = list(cnt.items())
cnt.sort()

ans = 0
for i in range(len(cnt)):
    k1, v1 = cnt[i]
    for j in range(len(cnt)):
        k2, v2 = cnt[j]
        if k1 == k2:
            ans += v1 * (v1 - 1) // 2
print(ans)