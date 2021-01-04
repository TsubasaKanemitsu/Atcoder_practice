a, b = list(map(int, input().split()))

# left = [[0 for i in range(b)] for j in range(a)]
# right = [0 for i in range(b)]

left = []
right = []
result = 0
for i in range(a):
        left.append(list(map(int, input().split())))

for i in range(b):
    right.append(int(input()))

for i in range(a):
    for j in range(b):
        result += left[i][j] * right[j]
    print(result)
    result = 0