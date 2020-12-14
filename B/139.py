a, b = list(map(int, input().split()))
x = 0
while a * x - (x - 1) < b:
    x += 1
print(x)