from collections import deque

S = input()
q = int(input())
query = [input().split() for _ in range(q)]

inv = 0
ans = deque(S)
for q in query:
    t = int(q[0])
    if t == 1:
        inv += 1
    elif t == 2:
        f = int(q[1])
        c = q[2]
        if inv % 2 == 0:
            if f == 1:
                ans.appendleft(c)
            elif f == 2:
                ans.append(c)
        elif inv % 2 == 1:
            if f == 1:
                ans.append(c)
            elif f == 2:
                ans.appendleft(c)
ans = list(ans)
if inv % 2 == 1:
    ans = ans[::-1]

print(''.join(ans))