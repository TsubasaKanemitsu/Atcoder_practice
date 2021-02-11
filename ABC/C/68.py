from collections import defaultdict
n, m = list(map(int, input().split()))
_bin = defaultdict(list)

for i in range(m):
    a, b = list(map(int, input().split()))
    _bin[a].append(b)

st = _bin[1]
for s in st:
    if n in _bin[s]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")