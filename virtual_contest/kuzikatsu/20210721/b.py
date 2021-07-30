from collections import defaultdict
n = int(input())

money = defaultdict(int)

for i in range(n):
    x, v = input().split()
    x = float(x)
    money[v] += x

ans = money['JPY'] + money['BTC'] * 380000
print(ans)