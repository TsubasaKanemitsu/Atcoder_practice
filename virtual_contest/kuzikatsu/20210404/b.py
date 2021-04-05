n = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
ans = 0
for i in range(n):
    for j in range(i, n):
        candie = sum(A[0][:i + 1]) + sum(A[1][i:])
        ans = max(ans, candie)
print(ans)