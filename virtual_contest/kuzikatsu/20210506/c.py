n = int(input())
a = list(map(int, input().split()))
a.sort()

b = a[n:]

ans = 0
for i in range(len(b)):
    if i % 2 == 0:
        ans += b[i]
print(ans)