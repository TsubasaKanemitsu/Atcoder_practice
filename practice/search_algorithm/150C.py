import itertools
n = int(input())

p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

a = 0
b = 0
count = 0
for perm in itertools.permutations(range(1, n + 1)):
    count += 1
    if perm == p:
        a = count
    if perm == q:
        b = count

print(abs(a - b))