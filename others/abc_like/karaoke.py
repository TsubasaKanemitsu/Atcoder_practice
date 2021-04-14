# 10分 全探索
n, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(m):
    for j in range(m):
        temp_ans = 0
        for k in range(n):
            if i != j:
                temp_ans += max(A[k][i], A[k][j])
        ans = max(ans, temp_ans)
print(ans)