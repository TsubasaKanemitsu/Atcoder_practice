from collections import Counter
n = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

cnt = list(cnt.items())
cnt.sort()
ans = 0

for i in range(len(cnt)):
    k1, v1 = cnt[i]
    for j in range(i + 1, len(cnt)):
        k2, v2 = cnt[j]
        ans += v1 * v2 * (k1 - k2) ** 2
print(ans)