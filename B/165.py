x = int(input())
money = 100
year = 0
while money < x:
    money += int(money // 100)
    year += 1
print(year)