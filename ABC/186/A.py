n, w = list(map(int, input().split()))

i = 0
while w * (i+1) <= n:
    i += 1
print(i)