import math
a, b, w = list(map(int, input().split()))

max_num = math.floor(w * 1000 / a)
min_num = math.ceil(w * 1000 / b)

if min_num <= max_num:
    print(min_num, max_num)
else:
    print("UNSATISFIABLE")