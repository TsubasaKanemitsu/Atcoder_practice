# 全探索
import itertools
from collections import defaultdict
n = int(input())
if n == 1:
    print(1)
    exit()

xy = [list(map(int, input().split())) for _ in range(n)]
cnt = defaultdict(int)

max_comb = 0
for (x1, y1), (x2, y2) in itertools.permutations(xy, 2):
    cnt[(x2 - x1, y2 - y1)] += 1
max_val = max(cnt.values())
ans = n - max_val
print(ans)