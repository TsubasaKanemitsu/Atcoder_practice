# ABC 160 C
# 15min
# 1WA

k, n = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = A[n - 1] - A[0]

for i in range(1, n):
    ans = min(ans, k - A[i] + A[i - 1])
print(ans)