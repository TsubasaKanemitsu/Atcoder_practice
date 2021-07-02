from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

ans = defaultdict(int)

for i in range(n):
    ans[(min(i + 1, A[i]), max(i + 1, A[i]))] += 1

cnt = 0

for k, v in ans.items():
    if v == 2:
        cnt += 1
print(cnt)
