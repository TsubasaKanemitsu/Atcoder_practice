n = int(input())
A = list(map(int, input().split()))

A.sort()

print(abs(A[0] - A[-1]))