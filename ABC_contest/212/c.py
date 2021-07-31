# ABC 212
# 二分探索(実装が苦手です)

import bisect
n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = list(set(B))
B.sort()

ans = 10 ** 99
for i in range(n):
    index = bisect.bisect_left(B, A[i])
    if index == 0:
        l_index = 0
        r_index = 0
    elif index == len(B):
        l_index = len(B) - 1
        r_index = len(B) - 1
    else:
        l_index = index - 1
        r_index = index
    ans = min(ans, abs(A[i] - B[l_index]), abs(A[i] - B[r_index]))
print(ans)