n, x = list(map(int, input().split()))
A = list(map(int, input().split()))

know = [False] * (n + 1)

cnt = 0
while not know[x]:
    know[x] = True
    cnt += 1
    x = A[x - 1]
print(cnt)