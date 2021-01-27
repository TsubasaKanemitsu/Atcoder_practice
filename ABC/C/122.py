# 29分
# 1WA
n, q = list(map(int, input().split()))
s = input()
l = []
r = []
for i in range(q):
    _l, _r = list(map(int, input().split()))
    l.append(_l)
    r.append(_r)

count_list = [0 for i in range(n)]
count = 0
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        count_list[i] = count
        count += 1
        count_list[i + 1] = count
    else:
        count_list[i] = count
        count_list[i + 1] = count
# print(count_list)

for i in range(q):
    print(count_list[r[i] - 1] - count_list[l[i] - 1])
