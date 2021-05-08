from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

cnt = defaultdict(int)

for i in range(n):
    num = sorted([i + 1, a[i]])
    cnt[(num[0], num[1])] += 1
ans = 0
for k, v in cnt.items():
    if v >= 2:
        ans += 1
print(ans)
