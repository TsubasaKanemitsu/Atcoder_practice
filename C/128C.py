import itertools

N, M = list(map(int, input().split()))

# matrix = [[0 for i in range(N + 1)] for j in range(N + 1)]
matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

p = []
p = list(map(int, input().split()))

print(matrix)
print(p)

for i in range(N):
    comb = itertools.combination(matrix[i], 2)
