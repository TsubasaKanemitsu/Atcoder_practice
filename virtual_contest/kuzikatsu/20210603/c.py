import math
a, b, c, d = list(map(int, input().split()))

lcm = c * d // math.gcd(c, d)

a_c = (a - 1) // c
a_d = (a - 1) // d
a_lcm = (a - 1) // lcm
aa = a_c + a_d - a_lcm

b_c = (b) // c
b_d = (b) // d
b_lcm = (b) // lcm
bb = b_c + b_d - b_lcm

ans = b - (a - 1) - (bb - aa)
print(ans)