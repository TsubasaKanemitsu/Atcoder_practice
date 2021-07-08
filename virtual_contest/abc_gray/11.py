# ABC 140
# 詰まった

n = int(input())
B = list(map(int, input().split()))

A = [0] * n
A[0] = B[0]
A[n - 1] = B[n - 2]

for i in range(1, n - 1):
    A[i] = min(B[i - 1], B[i])

print(sum(A))