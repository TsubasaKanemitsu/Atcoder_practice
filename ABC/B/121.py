n, m, c = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
for i in range(n):
    ans = 0
    a = list(map(int, input().split()))
    for j in range(m):
        ans += a[j] * b[j]
    ans += c
    if ans > 0:
        count += 1
print(count)