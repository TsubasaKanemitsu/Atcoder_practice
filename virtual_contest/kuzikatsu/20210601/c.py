n = int(input())
h = list(map(int, input().split()))

i = 0
cnt = 0
while True:
    
    water = False
    while h[i] > 0:
        water = True
        h[i] -= 1
        i += 1
        if i == n:
            break
    if water:
        cnt += 1

    if i >= n - 1:
        i = 0
    else:
        i += 1

    flag = True
    for j in range(n):
        if h[j] > 0:
            flag = False
    if flag:
        print(cnt)
        exit()