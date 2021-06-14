n, k, s = list(map(int, input().split()))

a = []
for i in range(n):
    if i < k:
        a.append(s)
    else:
        if s == 1:
            a.append(2)
        elif s == 10 ** 9:
            a.append(10 ** 9 - 1)
        else:
            a.append(s + 1)

for aa in a:
    print(aa, end=" ")