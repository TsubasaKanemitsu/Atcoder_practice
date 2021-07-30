# ABC 166 C
# 10min
# 1WA:問題読み間違え
from collections import defaultdict
n, m = list(map(int, input().split()))
H = list(map(int, input().split()))

path = defaultdict(list)
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    path[a].append(b)
    path[b].append(a)

ans = 0
for i in range(n):
    flag = True

    for h in path[i]:
        if H[i] <= H[h]:
            flag = False
    if flag:
        ans += 1
print(ans)