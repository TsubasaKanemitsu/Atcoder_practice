# 8分30秒

# 探索の開始位置(x,y)を決めて，AとBの比較を行うだけ
# O(N^2 * M^2)

n, m = list(map(int, input().split()))

A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(m)]

for i in range(n - m + 1):
    for j in range(n - m + 1):
        sy, sx = i, j
        cnt = 0
        for k in range(m):
            for l in range(m):
                if A[sy + k][sx + l] == B[k][l]:
                    cnt += 1
        if cnt == m * m:
            print("Yes")
            exit()
print("No")