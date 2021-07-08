# 若干手こずった
# 平均化していく過程で最大化するためには、一番大きい値は最後に平均化する必要がある。
# 7分

from collections import deque
n = int(input())
V = list(map(int, input().split()))
V.sort()
while len(V) > 1:
    v1 = V.pop(0)
    v2 = V.pop(0)
    V.append((v1 + v2) / 2)
    V.sort()
print(V[0])