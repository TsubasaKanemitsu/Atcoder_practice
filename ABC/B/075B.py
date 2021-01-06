# 爆弾の位置取得
def get_mine_pos(W, mine_index, input_data):
    mine_num = input_data.count('#')
    mine_count = 0
    mine_pos = []
    for i in range(W):
        if input_data[i] == '#':
            mine_pos.extend([[mine_index, i]])
            mine_count += 1
            if mine_count == mine_num:
                break
    return mine_pos


def get_adjacent_pos(i, j, H, W):
    
    adjacent_pos = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
    # print(adjacent_pos)
    result_pos = []
    for k in range(len(adjacent_pos)):
        if adjacent_pos[k][0] >= 0 and adjacent_pos[k][0] < H and adjacent_pos[k][1] >= 0 and adjacent_pos[k][1] < W:
            result_pos.extend([[adjacent_pos[k][0], adjacent_pos[k][1]]])

    return result_pos

H, W = list(map(int, input().split()))
S = []
mine_pos = []
mine_num = 0
_S = []
temp_S = []
for i in range(H):
    input_data = list(input())
    # 爆弾の位置取得
    if '#' in input_data:
        mine_pos.extend(get_mine_pos(W, i, input_data))
    S.append(input_data)

for i in range(H):
    for j in range(W):
        # 爆弾確認の位置
        adjacent_pos = get_adjacent_pos(i, j, H, W)
        # 爆弾の個数確認
        for k in range(len(adjacent_pos)):
            if S[adjacent_pos[k][0]][adjacent_pos[k][1]] == '#':
                mine_num += 1
        # 爆弾位置の場合
        if [i, j] in mine_pos:
            temp_S.append('#')
        else:
            temp_S.append(str(mine_num))
        mine_num = 0
    _S.extend([temp_S])
    temp_S = []

for i in range(len(_S)):
    print(''.join(_S[i]))

