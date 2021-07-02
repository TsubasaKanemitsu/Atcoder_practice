n, x = list(map(int, input().split()))

L = list(map(int, input().split()))

D = [0]
dist = 0
ans = 0
for i in range(n):
    D.append(D[i] + L[i])

for d in D:
    if d <= x:
        ans += 1
    else:
        print(ans)
        exit()
print(ans)