h, w = list(map(int, input().split()))

s = []
for i in range(h):
    s.append(list((input())))
print(s)

def is_check(x, y):
    dx = 1
    dy = 1
    if s[y][dx] < h and 
