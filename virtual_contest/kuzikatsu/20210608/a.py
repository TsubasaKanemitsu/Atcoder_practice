a, b, c, d = list(map(int, input().split()))

num = [a, b, c, d]

_sum = sum(num)

for bit in range(1 << len(num)):
    temp = 0
    for i in range(len(num)):
        if bit & 1 << i:
            temp += num[i]
    if temp == _sum - temp:
        print("Yes")
        exit()
print("No")