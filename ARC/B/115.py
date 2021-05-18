n = int(input())
C = [list(map(int, input().split())) for _ in range(n)]

mix = C[0][0]
miy = C[0][0]

for i in range(n):
    mix = min(mix, C[i][0])
    miy = min(miy, C[0][i])

X = []
Y = []
for i in range(n):
    X.append(C[i][0] - mix)
    Y.append(C[0][i] - miy)

# 差分を一律に足す
diff = C[0][0] - X[0] - Y[0]

for i in range(n):
    X[i] += diff

for i in range(n):
    for j in range(n):
        if X[i] + Y[j] != C[i][j]:
            print("No")
            exit()
print("Yes")
for i in range(n):
    print(X[i], end=" ")
print()
for i in range(n):
    print(Y[i], end=" ")