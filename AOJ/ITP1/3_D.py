a, b, c = list(map(int, input().split()))
divisor_num = 0
for i in range(a, b + 1):
    if c % i == 0:
        divisor_num += 1
print(divisor_num)