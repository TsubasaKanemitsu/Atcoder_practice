txa, tya, txb, tyb, T, V = list(map(int, input().split()))
n = int(input())

flag = False

for i in range(n):
    x, y = list(map(int, input().split()))
    dist1 = ((txa - x) ** 2 + (tya - y) ** 2) ** 0.5
    dist2 = ((txb - x) ** 2 + (tyb - y) ** 2) ** 0.5
    if dist1 + dist2 <= T * V:
        flag = True
if flag:
    print("YES")
else:
    print("NO")