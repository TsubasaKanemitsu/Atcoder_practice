# 4分30秒
n = int(input())
p = list(map(int, input().split()))

min_val = p[0]
cnt = 1
for i in range(1, n):
    if p[i] < min_val:
        cnt += 1
    min_val = min(min_val, p[i])
print(cnt)