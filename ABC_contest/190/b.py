n, s, d = list(map(int, input().split()))

flag = False

for i in range(n):
    x, y = list(map(int, input().split()))

    if x < s and d < y:
        flag = True

if flag:
    print("Yes")
else:
    print("No")