n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max_val = max(max(A), max(B))
C = [[False] * (max_val + 1) for _ in range(max_val + 1)]

for i in range(n):
    a = A[i]
    b = B[i]
    for c in range(a, b + 1):
        # とりえる値
        C[i][c] = True
