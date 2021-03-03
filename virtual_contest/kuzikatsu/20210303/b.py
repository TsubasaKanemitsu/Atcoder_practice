X, Y = list(map(int, input().split()))

for x in range(100):
    for y in range(100):
        if x + y == X and 2 * x + 4 * y == Y:
            print("Yes")
            exit()
print("No")