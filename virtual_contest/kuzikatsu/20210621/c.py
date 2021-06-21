# 解説もう一度読む
import math

n, m = list(map(int, input().split()))
S = list(input())
T = list(input())

lcm = n * m // math.gcd(n, m)
fn = n // math.gcd(n, m)
fm = m // math.gcd(n, m)

for i in range(math.gcd(n, m)):
    if S[fn * i] != T[fm * i]:
        print(-1)
        exit()
print(lcm)

