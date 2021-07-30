n = int(input())
s = input()

for i in range(n):
    if s[i] == '1' and i % 2 == 0:
        print("Takahashi")
        exit()
    elif s[i] == '1' and i % 2 == 1:
        print("Aoki")
        exit()