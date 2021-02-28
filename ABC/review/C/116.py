# 15分
n = int(input())
h = list(map(int, input().split()))

cnt = 0

i = 0
while True:
    if h[i] > 0:
        while h[i] > 0:
            h[i] -= 1
            if i == n - 1:
                break
            else:
                i += 1
        cnt += 1
    if i == n - 1:
        i = 0
        if sum(h) == 0:
            break
    else:
        i += 1
        
print(cnt)