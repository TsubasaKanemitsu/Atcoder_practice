from collections import deque

data = deque()

s = list(input())

for i in range(len(s)):
    if s[i] == '0':
        data.append(s[i])
    elif s[i] == '1':
        data.append(s[i])
    else:
        if len(data) > 0:
            data.pop()
print(''.join(data))
