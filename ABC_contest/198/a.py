from collections import defaultdict
n = int(input())
ans = defaultdict(int)
for i in range(1, n):
    ans[f'({i}, {n - i})'] += 1
    ans[f'({n - i}, {i})'] += 1

cnt = 0
for k, v in ans.items():
    cnt += 1
print(cnt)
