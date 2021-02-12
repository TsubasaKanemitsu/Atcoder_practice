from collections import Counter
s = input()

cnt = Counter(s)

if len(s) <= 2:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
else:
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - cnt:
            print("Yes")
            exit()
    print("No")
