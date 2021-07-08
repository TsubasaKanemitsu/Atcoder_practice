# 最後の処理に手間取った

n = int(input())
h = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(n - 1):
    if h[i] < h[i + 1]:
        ans = max(ans, cnt)
        cnt = 0
    else:
        cnt += 1
print(max(ans, cnt))