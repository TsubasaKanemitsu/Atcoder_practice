n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
BC = []
for i in range(m):
    b, c = list(map(int, input().split()))
    BC.append((b, c))
BC.sort(key=lambda x:x[1], reverse=True)

ans = 0
k = 0
flag = False
now = 0
for i in range(m):
    b, c = BC[i]
    for j in range(b):
        ans += max(A[k], c)
        k += 1
        if n <= k:
            flag = True
            break
    if flag:
        break

for i in range(k, n):
    ans += A[i]
print(ans)