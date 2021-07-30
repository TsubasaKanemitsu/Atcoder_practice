import bisect
# Bを固定するパターン
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
# AA = []
# BB = []
# CC = []
# for idx in range(n):
#     AA.append(idx, A[idx])
#     BB.append(idx, B[idx])
#     CC.append(idx, C[idx])

A.sort()
B.sort()
C.sort()

ans = 0
for i in range(n):
    if A[i] < B[i] < C[i]:
        ans += 1
print(ans)
