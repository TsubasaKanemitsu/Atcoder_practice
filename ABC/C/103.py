import math

def lcm(x, y):
    
    return (x * y) // math.gcd(x, y)

n = int(input())

A = list(map(int, input().split()))

lcm_val = A[0]
for i in range(1, len(A)):
    lcm_val = lcm(lcm_val, A[i])

ans = 0

for i in range(len(A)):
    ans += (lcm_val - 1) % A[i]
print(ans)
