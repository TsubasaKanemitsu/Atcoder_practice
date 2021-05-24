x = int(input())

num = 0
cnt = 0
for i in range(1, x + 1):
    ans = i * (i + 1) // 2
    cnt += 1
    if ans >= x:
        print(cnt)
        exit()