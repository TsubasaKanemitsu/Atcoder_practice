# 10分
sa = list(input())
sb = list(input())
sc = list(input())

now = "a"
while True:
    if now == 'a':
        if len(sa) == 0:
            print("A")
            exit()
        else:
            now = sa.pop(0)
    elif now == 'b':
        if len(sb) == 0:
            print("B")
            exit()
        else:
            now = sb.pop(0)
    elif now == 'c':
        if len(sc) == 0:
            print("C")
            exit()
        else:
            now = sc.pop(0)