import math

p = int(input()) * 0.01


def combinations_count(n, r):
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))


diff = 0
for i in range(4):
    diff += (p ** i) * combinations_count(7, i) * (1 - p) ** (7 - i)
    
print((1 - diff) * 100)