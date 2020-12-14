n, a, b = list(map(int, input().split()))
ans = 0

count = n // (a + b)
mod = n % (a + b) 
if mod <= a:
    blue = mod
if a < mod:
    blue = a

print(count * a + blue)
