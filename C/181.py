import itertools
n = int(input())

pos = []

for i in range(n):
    x, y = list(map(int, input().split()))
    pos.extend([[x, y]])

result = "No"
for perm in itertools.combinations(pos, 3):
   
    dx1 = perm[0][0] - perm[1][0]
    dy1 = perm[0][1] - perm[1][1]
    dx2 = perm[0][0] - perm[2][0]
    dy2 = perm[0][1] - perm[2][1]

    if dx1 * dy2 == dx2 * dy1:
        result = "Yes"
        break
print(result)
