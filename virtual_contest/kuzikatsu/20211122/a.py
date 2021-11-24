x = int(input())

if x < 100:
    print("No")
    exit()

if x % 100 != 0:
    print("No")
    exit()
print("Yes")