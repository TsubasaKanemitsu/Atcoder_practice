r, d, x_ = list(map(int, input().split()))

x_list = [x_]

for i in range(1, 11):
    x = r * x_list[i - 1] - d
    x_list.append(x)
    print(x)