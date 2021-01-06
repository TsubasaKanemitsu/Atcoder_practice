time = []
for i in range(5):
    time.append(int(input()))

min_mod = 9
last_dish = 0
for i in range(5):
    if time[i] % 10 > 0 and min_mod >= time[i] % 10:
        min_mod = time[i] % 10
        last_dish = time[i]
if last_dish == 0:
    last_dish = time[0]
time.remove(last_dish)

cumsum = 0
for i in range(len(time)):
    if time[i] % 10 > 0:
        cumsum += time[i] + (10 - time[i] % 10)
    else:
        cumsum += time[i]
cumsum = cumsum + last_dish

print(cumsum)
