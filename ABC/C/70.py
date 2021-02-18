# 5分
import math
def lcm(x, y):
    import math
    return (x * y) // math.gcd(x, y)

n = int(input())
T = [int(input()) for _ in range(n)]

lcm_num = T[0]

for t in T[1:]:
    lcm_num = lcm(lcm_num, t)
print(lcm_num) 