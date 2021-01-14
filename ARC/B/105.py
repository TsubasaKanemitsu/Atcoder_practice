n = int(input())

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

A = list(map(int, input().split()))

ans = A[0]
for a in A:
    ans = gcd(ans, a)

print(ans)