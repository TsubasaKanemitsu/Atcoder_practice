a, b, c, d = list(map(int, input().split()))

c_num = b // c - (a - 1) // c
d_num = b // d - (a - 1) // d

def lcm(a, b):
    import math
    return (a * b) // math.gcd(a, b)


cd_num = b // lcm(c, d) - (a - 1) // lcm(c, d)
cd_ans = c_num + d_num - cd_num

print(b - (a - 1) - cd_ans)