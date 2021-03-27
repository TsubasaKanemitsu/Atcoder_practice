n = int(input())

sum_n = 0

for i in range(1, 10):
    for j in range(1, 10):
        sum_n += i * j

diff = sum_n - n

ans = []

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == diff:
            ans.append([i, j])

for i, j in ans:
    print(str(i) + ' x ' + str(j))