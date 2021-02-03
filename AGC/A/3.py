s = input()

num = len(set(s))


if num == 1:
    print("No")
elif num == 2:
    n = s.count('N')
    e = s.count('E')
    w = s.count('W')
    S = s.count('S')
    if n >= 1 and S >= 1:
        print("Yes")
    elif e >= 1 and w >= 1:
        print("Yes")
    else:
        print("No")
elif num == 4:
    print("Yes")
else:
    print("No")
