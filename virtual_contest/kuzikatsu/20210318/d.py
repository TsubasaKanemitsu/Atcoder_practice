n = int(input())

xy = [list(map(int, input().split())) for _ in range(n)]

add = []
sub = []

for i in range(n):
    add.append(xy[i][0] + xy[i][1])
    sub.append(xy[i][0] - xy[i][1])

add.sort()
sub.sort()

print(max(abs(add[0] - add[-1]), abs(sub[0] - sub[-1])))
