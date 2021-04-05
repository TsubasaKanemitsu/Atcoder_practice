n = int(input())

for i in range(101):
    for j in range(101):
        ans = i * 4 + j * 7
        if ans == n:
            print("Yes")
            exit()
print("No")