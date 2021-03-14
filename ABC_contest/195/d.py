from collections import defaultdict
n, m, q = list(map(int, input().split()))

baggage = defaultdict[list]
for i in range(1, n + 1):
    w, v = list(map(int, input().split()))
    baggage[i] = [w, v]

x = defaultdict(int)
for i in range(1, m + 1):
    x[i] = int(input())

