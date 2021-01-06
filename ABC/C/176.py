n = int(input())
a = list(map(int, input().split()))
humidai = 0
for i in range(n - 1):
    if a[i] > a[i + 1]:
        humidai += a[i] - a[i + 1]
        a[i + 1] = a[i]
print(humidai)
