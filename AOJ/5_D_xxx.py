n = int(input())
list = []
for i in range(3, n + 1):
    if i % 3 == 0:
        list.append(i)
    else:
        x = i
        while x:
            if x % 10 == 3:
                list.append(i)
                break
            else:
                x = x // 10
print("", *list)


