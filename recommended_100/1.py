pattern = 0
n = []
x = []
while True:
    N, X = list(map(int, input().split()))
    if N == 0 and X == 0:
        break
    n.append(N)
    x.append(X)
    
for l in range(len(n)):
    for i in range(1, n[l] - 1):
        for j in range(i + 1, n[l]):
            for k in range(j + 1, n[l] + 1):
                if i != j and j != k and i + j + k == x[l]:
                    pattern += 1
    print(pattern)
    pattern = 0
