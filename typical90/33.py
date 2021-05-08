# 30分で解けない

h, w = list(map(int, input().split()))

hw = [['.'] * w for _ in range(h)]

if h == 1 and w == 1:
    print(1)
    exit()
elif h == 1 and w != 1:
    print(w)
    exit()
elif h != 1 and w == 1:
    print(h)
    exit()
else:
    cnt = 0
    for i in range(h):
        for j in range(w):
            if i % 2 == 0 and j % 2 == 0:
                hw[i][j] = '#'
                cnt += 1
    print(cnt)