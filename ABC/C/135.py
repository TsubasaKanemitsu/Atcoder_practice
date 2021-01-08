n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_val = 0
for i in range(n):

    if A[i] >= B[i]:
        sum_val += B[i]
    elif B[i] > A[i]:
        diff = B[i] - A[i]
        
        if diff > A[i + 1]:
            diff = A[i + 1]
        sum_val += A[i] + diff
        A[i + 1] = A[i + 1] - diff
    
print(sum_val)