from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

syusseki = []
for i in range(n):
    syusseki.append([a[i], i + 1])
syusseki.sort(key=lambda x:x[0])

for n, s in syusseki:
    print(s, end=' ')
print()