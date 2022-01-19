S = input()
T = input()

for k in range(27):
    ans = ''
    for s in S:
        num = (ord(s) + k % 26)
        if num > ord('z'):
            num = 96 + (num - ord('z'))
        ans += chr(num)
    if ans == T:
        print("Yes")
        exit()
print("No")