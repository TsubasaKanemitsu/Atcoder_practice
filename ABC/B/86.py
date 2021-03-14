a, b = input().split()

ab = int(a + b)

i = 1
while i * i <= ab:
    if ab % i == 0 and ab // i == i:
        print("Yes")
        exit()
    i += 1
print("No")