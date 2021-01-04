n = int(input())

tarou_point = 0
hanako_point = 0

for i in range(0, n):
    tarou, hanako = list(input().split())
    if tarou > hanako:
        tarou_point += 3
    elif tarou < hanako:
        hanako_point += 3
    else:
        tarou_point += 1
        hanako_point += 1
print(tarou_point, hanako_point)

# 13分