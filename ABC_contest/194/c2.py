from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

a_cnt = defaultdict(int)

for i in a:
    i += 200
    a_cnt[i] += 1

ans = 0
for i in range(401):
    for j in range(i + 1, 401):
        ans += a_cnt[i] * a_cnt[j] * (i - j) ** 2
# print(ans)

