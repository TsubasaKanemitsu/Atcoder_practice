k, s = list(map(int, input().split()))

cnt = 0
for i in range(k + 1):
    for j in range(k + 1):
        kk = s - i - j
        if 0 <= kk <= k:
            cnt += 1
print(cnt)