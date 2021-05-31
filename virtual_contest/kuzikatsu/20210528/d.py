k = int(input())

a = [10] * (k + 1)
a[0] = 7 % k
for i in range(1, k + 1):
    a[i] = (a[i - 1] * 10 + 7) % k

ans = -1
for i in range(k + 1):
    if a[i] == 0:
        ans = (i + 1)
        break
print(ans)