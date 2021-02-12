from collections import deque
s = deque(input())

Q = int(input())

st = 0
rev_cnt = 0
for i in range(Q):
    q = list(input().split())
    t = q[0]
    if t == '1':
        rev_cnt += 1
        if st == -1:
            st = 0
        else:
            st = -1
    elif t == '2':
        f = q[1]
        c = q[2]
        if f == '1':
            if st == 0:
                s.appendleft(c)
            else:
                s.append(c)
        elif f == '2':
            if st == 0:
                s.append(c)
            else:
                s.appendleft(c)
if rev_cnt % 2 == 1:
    s.reverse()
print(''.join(s))

