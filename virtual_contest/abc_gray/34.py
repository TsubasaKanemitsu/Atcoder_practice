# ABC 176 C
# 2WA
# 最大値更新

n = int(input())
A = list(map(int, input().split()))

ans = 0
max_ = A[0]
for i in range(1, n):
    if max_ < A[i]:
        max_ = A[i]
    else:
        ans += abs(max_ - A[i])
        
print(ans)