s = input()

for i in range(len(s)):
    if i % 2 == 0 and s[i].islower():
        pass
    elif i % 2 == 1 and s[i].isupper():
        pass
    else:
        print("No")
        exit()
print("Yes")