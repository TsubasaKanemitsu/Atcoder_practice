import math

L = int(input())

def combinations_count(n, r):
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))

print(combinations_count(L - 1, 11))