# 22分
# 全経路のうち，最大距離の経路を省く
k, n = list(map(int, input().split()))

A = list(map(int, input().split()))

# N件から最初の家まで
dist = [A[0] + (k - A[-1])]

for i in range(n - 1):
    dist.append(A[i + 1] - A[i])
ans = sum(dist) - max(dist)
print(ans)