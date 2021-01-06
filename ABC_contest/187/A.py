a, b = list(map(int, input().split()))

a = list(str(a))
a = list(map(lambda x: int(x), a))
b = list(str(b))
b = list(map(lambda x: int(x), b))

sum_a = sum(a)
sum_b = sum(b)

if sum_a >= sum_b:
    print(sum_a)
else:
    print(sum_b)
