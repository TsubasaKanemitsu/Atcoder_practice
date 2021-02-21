n = int(input())
num = [int(input()) for _ in range(5)]
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

def lcm(x, y):
    import math
    return (x * y) // math.gcd(x, y)

_lcm = lcm(num[0], num[1])
for i in range(2, 5):
    _lcm = lcm(_lcm, num[i])

cnt = 0
while n > 0:
    n -= _lcm
    cnt += 1
print(cnt * 5)
# print(n // _lcm)