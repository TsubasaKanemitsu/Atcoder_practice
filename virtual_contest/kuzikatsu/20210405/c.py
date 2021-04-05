n = int(input())
t = [int(input()) for _ in range(n)]

def lcm(x, y):
    import math
    return x * y // math.gcd(x, y)


_lcm = t[0]

for i in range(1, n):
    _lcm = lcm(_lcm, t[i])
print(_lcm)