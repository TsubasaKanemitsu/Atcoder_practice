from collections import defaultdict

n, m = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(m)]

union = set([i for i in range(1, n + 1)])
vv = defaultdict(dict)
for i in range(1, n + 1):
    vv[i] = union
print(vv)
