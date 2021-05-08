from collections import deque
S = input()

cnt = 0
T = deque()
length = 0
for i in range(len(S)):
    if S[i] == 'R':
        cnt += 1
    else:
        if cnt % 2 == 0:
            T.append(S[i])
            length += 1
            if length >= 2 and T[-1] == T[-2]:
                T.pop()
                T.pop()
                length -= 2
        else:
            T.appendleft(S[i])
            length += 1
            if length >= 2 and T[0] == T[1]:
                T.popleft()
                T.popleft()
                length -= 2

T = list(T)
if cnt % 2 == 1:
    T = T[::-1]
print(''.join(T))

