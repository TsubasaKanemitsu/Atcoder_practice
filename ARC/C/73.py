n, T = list(map(int, input().split()))
t = list(map(int, input().split()))

diff = []
for i in range(1, n):
    diff.append(t[i] - t[i - 1])

ans = 0
for i in range(n - 1):
    if T > diff[i]:
        ans += diff[i]
    else:
        ans += T
        
ans += T
print(ans)