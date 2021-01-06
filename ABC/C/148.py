import math
a, b = list(map(int, input().split()))

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm_base(a, b))


