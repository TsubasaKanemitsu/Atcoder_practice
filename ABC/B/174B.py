N, D = list(map(int, input().split()))
count = 0

for i in range(N):
    X, Y = list(map(int, input().split()))
    distance = (X ** 2 + Y ** 2) ** 0.5
    if distance <= D:
        count += 1

print(count)