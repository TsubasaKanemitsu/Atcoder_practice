# 9分30秒
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

color = defaultdict(int)
for a in A:
    if a >= 3200:
        color[8] += 1
    else:
        color[a // 400] += 1

ans = 0
for i in range(8):
    if color[i] > 0:
        ans += 1

if ans > 0:
    min_ans = ans
    max_ans = ans + color[8]
else:
    min_ans = 1
    max_ans = color[8]

print(min_ans, max_ans)
