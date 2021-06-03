n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = 0
for i in range(n - 1):
    if a[i] + a[i + 1] > x:
        diff = a[i] + a[i + 1] - x
        cnt += diff
    else:
        continue
    if diff <= a[i + 1]:
        a[i + 1] -= diff
    else:
        a[i + 1] = 0
        diff -= a[i + 1]
        a[i] -= diff
print(cnt)