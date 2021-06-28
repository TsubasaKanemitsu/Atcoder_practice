# 45分
# DP解けた

n = int(input())
ABC = [list(map(int, input().split())) for _ in range(n)]
ABC.insert(0, [0, 0, 0])

hapiness = [[0] * 3 for _ in range(n + 1)]

# 自分で書いた方法
# for i in range(1, n + 1):
#     for now_act in [0, 1, 2]:
#         for past_act in [0, 1, 2]:
#             if now_act == past_act:
#                 continue
#             hapiness[i][now_act] = max(hapiness[i][now_act], hapiness[i - 1][past_act] + ABC[i][now_act])

# print(max(hapiness[n]))

# 解説の方法 (こっちの方がわかりやすい)
for i in range(1, n + 1):
    hapiness[i][0] = max(hapiness[i][0], hapiness[i - 1][1] + ABC[i][1], hapiness[i - 1][2] + ABC[i][2])
    hapiness[i][1] = max(hapiness[i][1], hapiness[i - 1][0] + ABC[i][0], hapiness[i - 1][2] + ABC[i][2])
    hapiness[i][2] = max(hapiness[i][2], hapiness[i - 1][0] + ABC[i][0], hapiness[i - 1][1] + ABC[i][1])
print(max(hapiness[n]))