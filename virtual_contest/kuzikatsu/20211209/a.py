a, b, c = list(map(int, input().split()))

cnt = 0

if a == 0 and b == 0:
    if c % 2 == 0:
        print("Aoki")
    else:
        print("Takahashi")
    exit()

if c % 2 == 0:
    while a > 0 and b > 0:
        if cnt % 2 == 0:
            a -= 1
        else:
            b -= 1
        cnt += 1
else:
    while a > 0 and b > 0:
        if cnt % 2 == 0:
            b -= 1
        else:
            a -= 1
        cnt += 1

if a == 0:
    print("Aoki")
else:
    print("Takahashi")