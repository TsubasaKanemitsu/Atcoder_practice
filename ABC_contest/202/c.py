from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt_a = defaultdict(int)
cnt_bc = defaultdict(int)
for i in range(n):
    cnt_a[a[i]] += 1
    cnt_bc[b[c[i] - 1]] += 1

ans = 0
for i in range(1, n + 1):
    ans += cnt_a[i] * cnt_bc[i]
print(ans)