n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0
for i in range(n):
    ans += a[n + 2 * i]
print(ans)