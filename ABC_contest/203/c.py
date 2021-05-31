n, k = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort()
money = k
last_village = 0
for i in range(n):
    a, b = AB[i]
    # 前の村からの移動距離
    money -= a - last_village
    if money < 0:
        print(a + money)
        exit()
    money += b
    last_village = a

print(last_village + money)