k, s = list(map(int, input().split()))

count = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if z <= k and z >= 0:
            count += 1
print(count)