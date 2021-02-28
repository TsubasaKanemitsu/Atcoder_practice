# 7分
n, m = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(n)]

AB.sort(key=lambda x:x[0])

money = 0
for ab in AB:
    # 料金
    a = ab[0]
    # 本数
    b = ab[1]
    if m >= b:
        money += a * b
        m -= b
    else:
        money += a * m
        m = 0
    if m == 0:
        print(money)
        exit()