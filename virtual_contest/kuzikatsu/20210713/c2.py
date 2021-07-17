n = int(input())
A = list(map(int, input().split()))

xor_a = A[0]
for i in range(1, n):
    xor_a ^= A[i]

for i in range(n):
    print(xor_a ^ A[i], end=" ")