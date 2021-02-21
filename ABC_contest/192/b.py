s = input()

for i in range(len(s)):
    if (i + 1) % 2 == 1 and s[i].isupper():
        print("No")
        exit()
    if (i + 1) % 2 == 0 and s[i].islower():
        print("No")
        exit()
print("Yes")
            