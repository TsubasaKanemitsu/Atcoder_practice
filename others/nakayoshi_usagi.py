n = int(input())
a = list(map(int, input().split()))

ans = dict()
for i in range(len(a)):
    ans[i + 1] = a[i]

count = 0
for i in range(len(a)):
    key = i + 1
    value = ans[key]
    if ans[value] == key:
        count += 1

if count == 0:
    count = 0
else:
    count = count // 2
print(count)