a, b, c, d = list(map(int, input().split()))

for i in range(10 ** 6 + 1):
    if a + b * i <= d * c * i:
        print(i)
        exit()
    
print(-1)