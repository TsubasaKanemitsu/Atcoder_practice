import math
K = int(input())

sum_val = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            temp_gcd = math.gcd(i, j)
            gcd = math.gcd(temp_gcd, k)
            sum_val += gcd

print(sum_val)