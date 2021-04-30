import copy
n = int(input())
a = [int(input()) for _ in range(n)]

mx_a = 0
index = 0
for i in range(n):
    if a[i] > mx_a:
        mx_a = a[i]
        index = i

B = copy.deepcopy(a)
B.sort(reverse=True)
second_v = B[1]


for i in range(n):
    if i == index:
        print(second_v)
    else:
        print(mx_a)