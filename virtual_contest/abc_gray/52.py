# ABC 203 C
# 13min


n, k = list(map(int, input().split()))

AB = []

for i in range(n):
    a, b = list(map(int, input().split()))
    AB.append((a, b))

AB.sort()

money = k
pre = 0
for i in range(n):
    a, b = AB[i]
    if money >= a - pre:
        money = money - (a - pre) + b
        pre = a
    else:
        ans = pre + money
        print(ans)
        exit()
print(money + pre)