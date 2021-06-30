n, q = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

# 不便さの記録
B = [0] * (n + 1)
# ある地点における不便さ
ans = 0
for i in range(1, n):
    b = A[i + 1] - A[i]
    B[i] = b
    ans += abs(b)

ppr = []
for i in range(q):
    L, R, V = list(map(int, input().split()))
    
    before = abs(B[L - 1]) + abs(B[R])
    if L >= 2:
        B[L - 1] += V
    if R <= n - 1:
        B[R] -= V
    after = abs(B[L - 1]) + abs(B[R])

    ans += (after - before)

    ppr.append(ans)
    
for p in ppr:
    print(p)