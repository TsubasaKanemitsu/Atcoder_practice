n = int(input())

count = 0
ans = []
for i in range(1, n + 1, 2):
    for j in range(1, i + 1, 2):
        if i % j == 0:
            count += 1
    if count == 8:
        ans.append(i)
    count = 0
print(len(ans))