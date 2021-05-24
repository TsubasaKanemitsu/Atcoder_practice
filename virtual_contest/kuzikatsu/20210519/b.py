n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
a = []
b = []
for i in range(n):
    if i % 2 == 0:
        a.append(A[i])
    else:
        b.append(A[i])
print(sum(a) - sum(b))