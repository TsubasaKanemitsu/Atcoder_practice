# 6分30秒
n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if a[i] == cnt + 1:
        cnt += 1

ans = n - cnt

if n == ans:
    print(-1)
else:
    print(ans)
