n = int(input())
B = []
F = []
R = []
V = []
for i in range(n):
    b, f, r, v = list(map(int, input().split()))
    B.append(b)
    F.append(f)
    R.append(r)
    V.append(v)

count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(n):
    count[B[i] - 1][F[i] - 1][R[i] - 1] += V[i]
    
c = 0
for k in range(4):
    for j in range(3):
        for i in range(10):
            print('', count[k][j][i], end='')
        print()
        if j == 2 and c < 3:
            c += 1
            print('####################')