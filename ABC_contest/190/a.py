a, b, c = list(map(int, input().split()))

if c == 0:
    while True:
        a -= 1
        if a <= 0:
            print("Aoki")
            exit()
        b -= 1
        if b <= 0:
            print("Takahashi")
            exit()
elif c == 1:
    while True:
        b -= 1
        if b <= 0:
            print("Takahashi")
            exit()
        a -= 1
        if a <= 0:
            print("Aoki")
            exit()