from collections import deque
n = int(input())
a = list(input().split())

l = len(a)

b = deque()

for i in range(n):
    if (i + 1) % 2 == 1:
        b.append(a[i])
    else:
        b.appendleft(a[i])
    
if l % 2 == 0:
    print(' '.join(b))
else:
    print(' '.join(list(b)[::-1]))
