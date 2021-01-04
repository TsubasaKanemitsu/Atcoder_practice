from collections import deque

def push(data, pos, n):
    if pos == 0:
        data.appendleft(n)
    else:
        data.append(n)
    return data


def randomAccess(data, index):
    if data != []:
        return data[index]
    else:
        return []


def pop(data, pos):
    if data != []:
        if pos == 0:
            data.popleft()
        else:
            data.pop()
    return data

q = int(input())
data = deque()
ans = deque()
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        data = push(data, query[1], query[2])
    elif query[0] == 1:
        ans.append(randomAccess(data, query[1]))
    elif query[0] == 2:
        data = pop(data, query[1])

for i in ans:
    print(i)