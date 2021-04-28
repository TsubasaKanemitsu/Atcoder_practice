from collections import deque
sa = deque(input())
sb = deque(input())
sc = deque(input())

now = sa.popleft()
while True:
    if now == 'a':
        if len(sa) == 0:
            print('A')
            exit()
        else:
            now = sa.popleft()
    elif now == 'b':
        if len(sb) == 0:
            print('B')
            exit()
        else:
            now = sb.popleft()
    if now == 'c':
        if len(sc) == 0:
            print('C')
            exit()
        else:
            now = sc.popleft()


    