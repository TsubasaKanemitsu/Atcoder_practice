N = int(input())
count = 0
result = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1, 2):
        if i % j == 0:
            count += 1
    if count == 8:
        result += 1

print(result)