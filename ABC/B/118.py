N, M = list(map(int, input().split()))
like_list = []
# 好みの食物リスト
for i in range(N):
    KA = list(map(int, input().split()))
    like_list.append(KA[1:])

# 共通で好みの食物の抽出
ans = like_list[0]
for i in range(1, N):
    ans = list(set(ans) & set(like_list[i]))

print(len(ans))