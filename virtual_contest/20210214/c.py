n = int(input())
p = list(map(int, input().split()))

cnt = 0
for i in range(n - 1):
    if p[i] == i + 1:
        temp = p[i + 1]
        p[i + 1] = p[i]
        p[i] = temp
        cnt += 1
for i in range(n - 1, 0, -1):
    if p[i] == i + 1:
        temp = p[i]
        p[i - 1] = p[i]
        p[i - 1] = temp
        cnt += 1
print(cnt)