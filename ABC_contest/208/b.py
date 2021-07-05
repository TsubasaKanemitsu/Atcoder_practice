p = int(input())
money = [1]

for i in range(1, 10 ** 4 + 1):
    money.append(money[i - 1] * (i + 1))

ans = p
cnt = 0
for i in range(len(money) - 1, -1, -1):
    if ans - money[i] >= 0:
        while ans - money[i] >= 0:
            cnt += 1
            ans -= money[i]
        if ans == 0:
            print(cnt)
            exit()