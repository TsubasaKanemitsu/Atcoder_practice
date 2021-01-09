order = []
for i in range(5):
    order.append(int(input()))
order_mod_zero = [o for o in order if o % 10 == 0]
order_mod = [o for o in order if o % 10 != 0]
order_mod.sort(key=lambda x: x % 10, reverse=True)

sum_val = 0
if order_mod_zero:
    for o in order_mod_zero:
        sum_val += o

if order_mod:
    for i in range(len(order_mod) - 1):
        sum_val += order_mod[i] + (10 - order_mod[i] % 10)
    sum_val += order_mod[-1]
print(sum_val)