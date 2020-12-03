flag = 1
i = 0
N = []
X = []
while flag > 0:
    n, x = list(map(int, input().split()))
    if n == 0 and x == 0:
        flag = -1
    else:
        N.append(n)
        X.append(x)
        i += 1
for c in range(len(N)):
    result = []
    for i in range(1, N[c] + 1):
        for j in range(i + 1, N[c] + 1):
            for k in range(j + 1, N[c] + 1):
                sm = i + j + k
                if i != j and j != k and i != k and sm == X[c]:
                    result.append([i, j, k])
    print(len(result))