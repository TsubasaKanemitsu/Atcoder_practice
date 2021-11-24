s = list(input())

num = len(set(s))

if num == 1:
    print(1)
elif num == 2:
    print(3)
else:
    print(6)