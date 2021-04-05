from collections import defaultdict
n = int(input())
a = [int(input()) for _ in range(n)]

button = defaultdict(int)
for i in range(1, n + 1):
    button[i] = a[i - 1]

cnt = 0
now = 1
while cnt <= n:
    if button[now] == 2:
        cnt += 1
        print(cnt)
        exit()
    else:
        now = button[now]
        cnt += 1
print(-1)