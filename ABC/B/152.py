a, b = list(map(int, input().split()))

A = str(a) * b
B = str(b) * a

if A > B:
    print(B)
else:
    print(A)
