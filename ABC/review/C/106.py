s = input()
k = int(input())
if len(s) == 1:
    print(s)
else:
    if s[0] == '1':
        for i in range(len(s)):
            if i == k:
                print(1)
                exit()
            if s[i] != '1':
                break
        print(s[i])
    else:
        print(s[0])