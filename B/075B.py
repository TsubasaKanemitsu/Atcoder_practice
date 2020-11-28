# 途中です
H, W = list(map(int, input().split()))

result = []
for S in range(H):
    result.append(list(input()))

answer = ''
mine = 0
for i in range(H):
    for j in range(W):
        pos = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
        for num in range(len(pos)):
            # print(result[1, 1])
            if pos[num][0] >= 0  and pos[num][0] < H and pos[num][1] >= 0 and pos[num][1] < W:
                # print(pos[num][0], pos[num][1])
                if result[pos[num][0]][pos[num][1]] == '#':
                    mine += 1
        answer = answer.join(str(mine))
        mine = 0
    print(answer)
