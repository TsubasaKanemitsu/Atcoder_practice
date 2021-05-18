n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]

txy.insert(0, [0, 0, 0])

flag = True
for i in range(1, n + 1):
    t1, x1, y1 = txy[i - 1]
    t2, x2, y2 = txy[i]
    if (t2 - t1) >= abs(x2 - x1) + abs(y2 - y1) and (t2 - t1) % 2 == (abs(x2 - x1) + abs(y2 - y1)) % 2:
        pass
    else:
        flag = False
if flag:
    print("Yes")
else:
    print("No")