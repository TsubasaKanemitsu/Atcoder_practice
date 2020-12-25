k, n = list(map(int, input().split()))

a = list(map(int, input().split()))

dist = k - a[n - 1] + a[0]

for i in range(n - 1):
    dist = max(dist, a[i + 1] - a[i])

print(k - dist)