import itertools

order = []
for i in range(5):
    order.append(int(input()))

sum_val = 643
for perm in itertools.permutations(order, len(order)):
    temp_sum = 0
    for i in range(len(perm) - 1):
        if perm[i] % 10 != 0:
            temp_sum += perm[i] + (10 - perm[i] % 10)
        else:
            temp_sum += perm[i]
    temp_sum += perm[-1]
    sum_val = min(sum_val, temp_sum)
print(sum_val)