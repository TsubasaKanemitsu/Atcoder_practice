from collections import deque
S = list(input())
# 反転という行為は次の動作で追加があるときに
# 先頭か末尾に追加かを変更すればいい

# cntが奇数の時は先頭、偶数の時は末尾
cnt = 0
# 先頭の2文字 or 末尾の2文字が同じときは排除する


T = deque()

for s in S:
    if s == 'R':
        cnt += 1
    else:
        if cnt % 2 == 0:
            T.append(s)
        else:
            T.appendleft(s)
    if len(T) >= 2:
        if T[0] == T[1]:
            T.popleft()
            T.popleft()
        elif T[-2] == T[-1]:
            T.pop()
            T.pop()

T = list(T)
if cnt % 2 == 1:
    T = T[::-1]

print(''.join(T))