N = int(input())
money = 0

for i in range(N):
    x, u = input().split()
    x = float(x)
    if u == "BTC":
        money += x * 380000
    else:
        money += x
print(money)