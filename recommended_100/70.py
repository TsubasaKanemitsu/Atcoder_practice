# 繰り返し2乗法
m, n = list(map(int, input().split()))
print(pow(m, n, 10 ** 9 + 7))

# nn = n
# bit = []

# while n != 0:
#     bit.append(n % 2)
#     n = n // 2

# ans = 1
# for i in range(len(bit)):
#     if bit[i] == 1:
#         ans = 
#         ans % (10 ** 9 + 7) * m ** (2 ** i)
# print(ans % (10 ** 9 + 7))