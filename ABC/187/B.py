n = int(input())

pos = []

for i in range(n):
    pos.extend([list(map(int, input().split()))])

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        dx = pos[j][0] - pos[i][0]
        dy = pos[j][1] - pos[i][1]
        kt = dy / dx
        if -1 <= kt <= 1:
            count += 1
print(count)