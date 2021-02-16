# シミュレーション
# いもす法
from collections import defaultdict
n, w = list(map(int, input().split()))
event = defaultdict(int)
for i in range(n):
    s, t, p = list(map(int, input().split()))
    event[s] += p
    event[t] -= p

event = sorted(event.items(), key=lambda x: x[0])

pre = 0
now = 0
for k, v in event:
    now += v
    if now > w:
        print("No")
        exit()
print("Yes")
