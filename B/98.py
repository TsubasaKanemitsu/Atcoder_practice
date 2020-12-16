N = int(input())
S = list(input())
ans = 0
for i in range(1, N):
    X = S[0:i]
    Y = S[i:]
    common_word_num = len(list(set(X) & set(Y)))
    ans = max(ans, common_word_num)
print(ans)

# set(x) & set(y) -> x, y の共通要素の抽出
# set(x) ^ set(y) -> x, y のどちらか片方に含まれる要素の抽出
