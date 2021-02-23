# 30分
w, h, n = list(map(int, input().split()))

x_lim = 0
y_lim = 0
s = [['.' for _ in range(w)] for _ in range(h)]

for i in range(n):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        for i in range(x):
            for j in range(h):
                s[j][i] = '#'
    elif a == 2:
        for i in range(x, w):
            for j in range(h):
                s[j][i] = '#'
    elif a == 3:
        for i in range(w):
            for j in range(y):
                s[j][i] = '#'
    else:
        for i in range(w):
            for j in range(y, h):
                s[j][i] = '#'

cnt = 0
for i in range(w):
    for j in range(h):
        if s[j][i] == '.':
            cnt += 1
print(cnt)