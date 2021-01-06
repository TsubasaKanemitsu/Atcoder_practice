n = int(input())

s = input()

if len(s) % 2 == 0:
    i = len(s) // 2
    if s[0:i] == s[i:]:
        print("Yes")
    else:
        print("No")

else:
    print("No")