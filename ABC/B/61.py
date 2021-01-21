from collections import Counter

n, m = list(map(int, input().split()))

city = [0 for i in range(n + 1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    city[a] += 1
    city[b] += 1

for val in city[1:]:
    print(val)