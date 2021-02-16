# いもす法
from collections import defaultdict
n, w = list(map(int, input().split()))

event = defaultdict(int)
last = 0
for i in range(n):
    s, t, p = list(map(int, input().split()))
    event[s] += p
    event[t] -= p
    last = max(last, t)

cum_sum = [0 for _ in range(last + 1)]
cum_sum[0] = event[0]
if event[0] > w:
    print("No")
    exit()
else:
    for i in range(1, last + 1):
        cum_sum[i] = event[i] + cum_sum[i - 1]
        if cum_sum[i] > w:
            print("No")
            exit()
    print("Yes")
