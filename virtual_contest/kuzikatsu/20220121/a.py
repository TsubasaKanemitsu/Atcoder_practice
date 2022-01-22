from numpy import iinfo


n = int(input())
A = [int(input()) for _ in range(n)]

max_val1 = max(A)
B = A.copy()
B.remove(max_val1)
max_val2 = max(B)

if max_val1 == max_val2:
    for _ in range(n):
        print(max_val1)
else:
    for a in A:
        if a == max_val1:
            print(max_val2)
        else:
            print(max_val1)