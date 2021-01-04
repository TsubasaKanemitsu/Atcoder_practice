def pushBack(data, n):
    data.append(n)
    return data


def randomAccess(data, index):
    return data[index]


def popBack(data):
    if data != []:
        data.pop()
    return data

q = int(input())
data = []
ans = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        data = pushBack(data, query[1])
    elif query[0] == 1:
        ans.append(randomAccess(data, query[1]))
    elif query[0] == 2:
        data = popBack(data)

for i in ans:
    print(i)