from collections import defaultdict
n, m = list(map(int, input().split()))

abc = defaultdict(list)

for _ in range(m):
    a, b, c = list(map(int, input().split()))
    abc[(a, b)] = c
    abc[(b, a)] = c

min_val = 10 ** 100
for key, val in abc.items():
    min_val = min(val, min_val)
print(min_val)
ans = set()
miss = set()
for key, val in abc.items():
    if val != min_val:
        a = min(key)
        b = max(key)
        ans.add((a, b))
    else:
        miss.add((a, b))
print(ans, miss)
ans = ans - miss
print(len(ans))
