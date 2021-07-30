import math
a, b = list(map(int, input().split()))

# 消費税が最大100なので、ループの最大数は、1000でいい。
for i in range(1, 10 ** 6):
    A = math.floor(i * 0.08)
    B = math.floor(i * 0.1)
    if a == A and b == B:
        print(i)
        exit()
print(-1)