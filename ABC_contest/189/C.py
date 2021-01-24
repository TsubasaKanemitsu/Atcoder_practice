n = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(n):
    x = A[l]
    r = l
    for r in range(r, n):
        x = min(x, A[r])
        ans = max(ans, x * (r - l + 1))
print(ans)