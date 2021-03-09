n = int(input())

p = 0

for i in range(1, n):
    p +=  n / (n - i)
print(p)