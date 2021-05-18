from decimal import Decimal
a, b = list(map(int, input().split()))

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b > 0:
        a, b = b, a % b
    return b

def lcm(x, y):
    x = Decimal(str(x))
    y = Decimal(str(y))
    return x * y / gcd(x, y)


ans = lcm(a, b)
if ans > 10 ** 18:
    print("Large")
    exit()
print(int(ans))