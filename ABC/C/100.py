n = int(input())

A = list(map(int, input().split()))
count = 0
for i in range(len(A)):
    while A[i] % 2 == 0:
        if A[i] % 2 == 0:
            A[i] /= 2
            count += 1

print(count)

