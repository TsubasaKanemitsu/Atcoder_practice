n = int(input())

A = list(map(int, input().split()))

c4 = 0
c2 = 0
c1 = 0

for a in A:
    if a % 4 == 0:
        c4 += 1
    elif a % 2 == 0:
        c2 += 1
    else:
        c1 += 1

if c4 >= c1:
    print("Yes")
elif c4 == c1 - 1 and c2 == 0:
    print("Yes")
else:
    print("No")