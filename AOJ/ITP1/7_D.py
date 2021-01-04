n, m, l = list(map(int, input().split()))

A = [[0 for i in range(m)] for j in range(n)]
B = [[0 for i in range(l)] for j in range(m)]
C = [[0 for i in range(l)] for j in range(n)]

for j in range(n):
    A[j] = (list(map(int, input().split())))

for i in range(m):
    B[i] = (list(map(int, input().split())))

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]

for i in range(len(C)):
    result = list(map(lambda x: str(x), C[i]))
    print(' '.join(result))