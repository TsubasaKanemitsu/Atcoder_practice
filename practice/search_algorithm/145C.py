import itertools

def permutaions_count(n, r):
    import math
    ans = math.factorial(n) // math.factorial(n - r)
    return ans 

n = int(input())

z = []
for i in range(n):
    x, y = list(map(int, input().split()))
    z.append([x, y])

sum_val = 0
for perm in itertools.permutations(z):
    for i in range(len(perm) - 1):
        length = ((perm[i][0] - perm[i + 1][0]) ** 2 + (perm[i][1] - perm[i + 1][1]) ** 2) ** 0.5
        sum_val += length

print(sum_val / permutaions_count(n, n))
