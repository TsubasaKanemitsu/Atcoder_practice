n = int(input())

time = 0
money = 10 ** 9
prev = 0
for i in range(n):
    a, p, x = list(map(int, input().split()))
    time += a - prev
    prev = a
    stock = x - time
    if stock > 0:
        money = min(p, money)
if money == 10 ** 9:
    print(-1)
else:
    print(money)