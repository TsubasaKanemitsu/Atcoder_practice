n = int(input())

result = "Yes"
temp_x = 0
temp_y = 0
temp_t = 0
for i in range(n):
    t, x, y = list(map(int, input().split()))
    diff_x = abs(x - temp_x)
    diff_y = abs(y - temp_y)
    diff_t = t - temp_t
    diff = diff_x + diff_y

    if diff_t >= diff and (diff_t - diff) % 2 == 0:
        pass
    else:
        result = "No"
    temp_x = x
    temp_y = y
    temp_t = t

print(result)

