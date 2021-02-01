n, m, x = list(map(int, input().split()))

num_list = [i for i in range(n)]

c = []
a = []
for i in range(n):
    data = list(map(int, input().split()))
    c.append(data[0])
    a.append(data[1:])

money = 10 ** 99
for bit in range(1 << len(num_list)):
    temp_sum = [0 for j in range(m)]
    temp_money = 0
    for i in range(len(num_list)):
        if bit & (1 << i):
            for j in range(m):
                temp_sum[j] += a[i][j]
            temp_money += c[i]

    flag = True
    for j in range(m):
        if temp_sum[j] < x:
            flag = False

    if flag:
        money = min(money, temp_money)

if flag:
    print(money)
else:
    print(-1)