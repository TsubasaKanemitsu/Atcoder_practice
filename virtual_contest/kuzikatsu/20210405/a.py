a, b = list(map(int, input().split()))

for k in range(1, 4):
    ans = a * b * k
    if ans % 2 == 1:
        print("Yes")
        exit()

print("No")