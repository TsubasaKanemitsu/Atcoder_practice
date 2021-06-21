n = int(input())

a = 206

ans = int(1.08 * n)

if ans < a:
    print("Yay!")
elif ans == a:
    print("so-so")
else:
    print(":(")