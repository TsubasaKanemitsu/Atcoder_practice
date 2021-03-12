n = int(input())
h = list(map(int, input().split()))
cnt = 1
max_val = h[0]
for i in range(1, n):
    if max_val <= h[i]:
        cnt += 1
        max_val = h[i]
print(cnt)