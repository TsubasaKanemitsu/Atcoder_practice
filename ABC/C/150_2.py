# 4分30秒
import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

pp = list(itertools.permutations(range(1, n + 1), n))
count = 0
for perm in pp:
    count += 1
    if perm == p:
        a = count
    if perm == q:
        b = count
print(abs(a - b))