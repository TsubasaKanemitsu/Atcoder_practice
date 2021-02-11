n, m = list(map(int, input().split()))
X = list(map(int, input().split()))

X.sort()

if n >= m:
    print(0)
else:
    diff = []
    for i in range(1, m):
        diff.append(X[i] - X[i - 1])
    diff.sort()
    ans = diff[0:m - n]
    print(sum(ans))