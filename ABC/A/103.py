A = list(map(int, input().split()))

A.sort(reverse=True)
print(abs(A[0] - A[1]) + abs(A[1] - A[2]))