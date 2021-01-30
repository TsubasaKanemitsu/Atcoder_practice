import itertools
n, m = list(map(int, input().split()))

dish_list = [list(map(int, input().split())) for _ in range(m)]

k = int(input())
select_dish_list = [list(map(int, input().split())) for _ in range(k)]

count = 0
for balls in itertools.product(*select_dish_list):
    balls = set(balls)
    temp_count = 0
    for i in range(m):
        if set(dish_list[i]) <= balls:
            temp_count += 1
    count = max(count, temp_count)
print(count)