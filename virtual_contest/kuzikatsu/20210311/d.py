# 最初の状態と更新する対象と状態繊維を考え，それぞれ定義する必要がある

n, m = list(map(int, input().split()))

xy = [list(map(int, input().split())) for _ in range(m)]

balls = [1 for _ in range(n)]

red = [False] * n
red[0] = True

# ballのある可能性
# pos_ball = set({0})

# for x, y in xy:
#     x -= 1
#     y -= 1
#     if x in pos_ball:
#         if balls[x] >= 1 and y not in pos_ball:
#             pos_ball.add(y)
#         red_pos = y
#     balls[x] -= 1
#     balls[y] += 1
        
#     if balls[x] == 0:
#         pos_ball.discard(x)
# print(len(pos_ball))

# 取り出す箱に赤い玉が入っていたら，次に入れる箱は赤い玉が入っている可能性がある．
# 前提条件とその前提条件が満たされた場合に，どのような状態遷移を行うのかを考えればいい
for x, y in xy:
    x -= 1
    y -= 1
    if red[x]:
        red[y] = True
    balls[x] -= 1
    balls[y] += 1
    if balls[x] == 0:
        red[x] = False

print(red.count(True))