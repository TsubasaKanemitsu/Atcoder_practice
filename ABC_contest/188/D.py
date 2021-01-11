# いもす法の応用
from collections import defaultdict
n, C = list(map(int, input().split()))

A = []
B = []
event = defaultdict(int)
for i in range(n):
    a, b, c = list(map(int, input().split()))
    event[a] += c
    event[b + 1] -= c
event = sorted(event.items(), key=lambda x: x[0])
print(event)

s = 0
ans = 0
pre = 0
for k, v in dict(event).items():
    print(k, pre, s, ans)
    ans += min(C, s) * (k - pre)
    s += v
    pre = k
print(ans)