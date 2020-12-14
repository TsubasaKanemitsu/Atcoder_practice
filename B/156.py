n, k = list(map(int, input().split()))
digit = 0
while n > 0:
    n = n // k
    digit += 1

print(digit)