import math
a, b = list(map(int, input().split()))

x_a = a // 0.08 + 1
x_b = b // 0.1 + 1
max_val = int(max(x_a, x_b))

for i in range(1, max_val + 1):
    if  math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        print(i)
        exit()
print(-1)