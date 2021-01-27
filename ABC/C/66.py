# 26分
from collections import deque
n = int(input())
a = list(map(int, input().split()))

ans = deque()

# for i in range(n):
#     if i % 2 == 0:
#         ans.append(a[i])
#     else:
#         ans.appendleft(a[i])

# if len(ans) % 2 == 1:
#     ans = list(ans)
#     ans = ans[::-1]

for i in range(n):
    if i % 2 == (n - 1) % 2:
        ans.appendleft(a[i])
    else:
        ans.append(a[i])

for i in ans:
    print(i, '', end='')
