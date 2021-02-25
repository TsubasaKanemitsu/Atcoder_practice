import itertools
n = list(input().split())

for perm in itertools.permutations(n, 4):
    word = ''.join(perm)
    if word == '1974':
        print("YES")
        exit()
print("NO")