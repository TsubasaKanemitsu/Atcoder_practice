n, h, w = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for ab in AB:
    if ab[0] >= h and ab[1] >= w:
        cnt += 1

print(cnt)