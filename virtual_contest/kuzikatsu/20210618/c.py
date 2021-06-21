n = int(input())
A = list(map(int, input().split()))

A.sort()

div = A[n//2] / 2

ans = 0
for i in range(n): 
    ans += div + A[i] - min(A[i], A[n // 2])
print(ans / n)

