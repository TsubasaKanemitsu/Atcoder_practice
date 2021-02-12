# 12分
# 1WA
from collections import Counter
n = int(input())
s = [input() for _ in range(n)]

cnt = Counter(s)

max_val = max(cnt.values())
max_k_list = sorted([kv[0] for kv in cnt.items() if kv[1] == max_val])

for k in max_k_list:
    print(k)
