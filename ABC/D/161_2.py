# https://drken1215.hatenablog.com/entry/2020/04/05/150900
from collections import deque

k = int(input())

Q = deque()
for i in range(1, 10):
    Q.append(i)

ans = []
for _ in range(k):
    num = Q.popleft()
    ans.append(num)

    for j in range(- 1, 2):
        add = num % 10 + j
        if 0 <= add <= 9:
            Q.append(num * 10 + add)
print(ans[k - 1])