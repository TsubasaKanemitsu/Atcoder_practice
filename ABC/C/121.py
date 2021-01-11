n, m = list(map(int, input().split()))
data = []
for i in range(n):
    a, b = list(map(int, input().split()))
    data.append((a, b))

data.sort()

money = 0
for i in data:
    if m >= i[1]:
        m -= i[1]
        money += i[0] * i[1]
    else:
        money += m * i[0]
        break
print(money)
