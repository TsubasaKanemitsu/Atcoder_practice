# from collections import deque
n, m, k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [A[0]]
b = [B[0]]

for i in range(1, n):
    a.append(a[i - 1] + A[i])
for i in range(1, m):
    b.append(b[i - 1] + B[i])
a.insert(0, 0)
b.insert(0, 0)

ans = 0
j = m
for i in range(n + 1):
    if a[i] > k:
        break
    while b[j] > k - a[i]:
        j -= 1
    ans = max(ans, i + j)
    
print(ans)
