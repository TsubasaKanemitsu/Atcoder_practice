n = int(input())

h = list(map(int, input().split()))

count = 0
for i in range(len(h)):
    flag = True
    for j in range(i):
        if h[j] > h[i]:
            flag = False
    if flag:
        count += 1
print(count)