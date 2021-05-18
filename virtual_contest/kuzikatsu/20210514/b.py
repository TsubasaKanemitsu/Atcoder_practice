from collections import defaultdict
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

cnt_a = defaultdict(int)
for a in A:
    cnt_a[a] += 1

ans = 0
for i in range(n):
    ans += (k - min(k, cnt_a[i])) * i
    k = min(k, cnt_a[i])
print(ans)