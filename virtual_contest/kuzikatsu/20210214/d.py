h, w = list(map(int, input().split()))

shape = []

def check_black(x, y, Shape):
    Dx = (0, 1)
    Dy = (0, 1)
    Cnt = 0
    result = False
    for dy in Dy:
        for dx in Dx:
            temp_x = x + dx
            temp_y = y + dy
            if shape[temp_y][temp_x] == '#':
                Cnt += 1
    if Cnt == 3 or Cnt == 1:
        result = True
    return result
        

for i in range(h):
    shape.append(list(input()))


cnt = 0
for y in range(h - 1):
    for x in range(w - 1):
        if check_black(x, y, shape):
            cnt += 1
            
print(cnt)
