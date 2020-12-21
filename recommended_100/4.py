n, m = list(map(int, input().split()))
A = []
ans = 0
for i in range(n):
    A.extend([list(map(int, input().split()))])

for i in range(m):
    for j in range(i + 1, m):
        score = 0
        for k in range(n):
            score += max(A[k][i], A[k][j])
        ans = max(ans, score)
print(ans)