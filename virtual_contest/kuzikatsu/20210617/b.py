s = input()

for i in range(len(s)):
    if i % 2 == 0 and s[i] == "L":
        print("No")
        exit()
    elif i % 2 == 1 and s[i] == "R":
        print("No")
        exit()
print("Yes")