# 6分
n, k, q = list(map(int, input().split()))

A = [int(input()) for _ in range(q)]

point = [k] * n

for i in range(q):
    a = A[i]
    point[a - 1] += 1

for i in range(n):
    if point[i] > q:
        print("Yes")
    else:
        print("No")