matrix = []
for i in range(2):
    matrix.extend([list(map(int, input().split()))])

det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

print(det)