x = input()
xx = sum(list(map(int, x)))
x = int(x)

if x % xx == 0:
    print("Yes")
else:
    print("No")