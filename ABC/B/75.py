h, w = list(map(int, input().split()))
s = []
for i in range(h):
    s.extend([list(input())])

pos_list = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

def is_pos_check(pos, h, w):
    if 0 <= pos[0] < h and 0 <= pos[1] < w:
        return True
    else:
        return False

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            pass
        else:
            bom_count = 0
            for pos in pos_list:
                if is_pos_check([i + pos[0], j + pos[1]], h, w):
                    if s[i + pos[0]][j + pos[1]] == '#':
                        bom_count += 1
            s[i][j] = str(bom_count)

for i in s:
    print(''.join(i))