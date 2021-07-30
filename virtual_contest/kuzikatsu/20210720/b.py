n, k, q = list(map(int, input().split()))

A = [0] * n
for _ in range(q):
    a = int(input())
    a -= 1
    A[a] += 1

for i in range(n):
    if A[i] + k - q > 0:
        print("Yes")
    else:
        print("No")