import itertools

n = int(input())
a = list(map(int, input().split()))
b = [i + 1 for i in a]
c = [i - 1 for i in a]

_list = []
for i in range(n):
    _list.append([a[i], b[i], c[i]])


count = 0
for comb in itertools.product(*_list):
    ans = 1
    ans2 = 0
    for c in comb:
        ans *= c
    if ans % 2 == 0:
        count += 1
print(count)

# 別解
# odd = 1
# for i in a:
#     if i % 2 == 0:
#         odd *= 2
# print(3 ** n - odd)