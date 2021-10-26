a, b, c = list(map(int, input().split()))

for i in range(1, 1001):
    if i * c > b:
        print(-1)
        exit()
    if a <= i * c <= b:
        print(i * c)
        exit()
