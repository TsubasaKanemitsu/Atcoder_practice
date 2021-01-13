h, w = list(map(int, input().split()))

s = [list(input()) for _ in range(h)]

def color_check(s, dx, dy, h, w):
    position = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    check_flag = False
    for pos in position:
        if 0 <= dx + pos[0] < h and 0 <= dy + pos[1] < w and s[dx + pos[0]][dy + pos[1]] == '#':
            check_flag = True
    return check_flag

def my_color_check(mark):
    if mark == '#':
        return 'black'
    else:
        return 'white'

for i in range(h):
    for j in range(w):
        if my_color_check(s[i][j]) == 'black':
            if not color_check(s, i, j, h, w):
                print("No")
                exit()
            else:
                pass
print("Yes")
