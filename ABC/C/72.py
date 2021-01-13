from collections import defaultdict
n = int(input())
N = list(map(int, input().split()))

for i in range(n):
    N.append(N[i] + 1)
    N.append(N[i] - 1)

d = defaultdict(int)
for num in N:
    d[num] += 1

print(max(list(d.values())))
