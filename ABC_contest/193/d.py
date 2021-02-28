from collections import defaultdict
k = int(input())
s = input()[:4]
t = input()[:4]

# カードの枚数
card = [k] * 10
for c in s:
    card[int(c)] -= 1
for c in t:
    card[int(c)] -= 1

# ポイント計算
def score(S):
    cnt = [0] * 10
    for s in S:
        cnt[int(s)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * 10 ** cnt[i]
    return ans

# 選ぶカードが異なる場合
ans = 0
for i in range(1, 10):
    if card[i] == 0:
        continue
    for j in range(1, 10):
        # 青木君が選べるカードの残り枚数が0の時と，高橋君と同じカードを選ぶパターンを
        # 排除している
        if card[j] == 0 or i == j:
            continue
        if score(s + str(i)) > score(t + str(j)):
            ans += card[i] * card[j]

# 選ぶカードが同じ場合
for i in range(1, 10):
    # 1枚か0枚しか残っていない場合，高橋君と青木君が同じカードを引ける可能性は
    # 残っていないため，continueする
    if card[i] < 2:
        continue
    if score(s + str(i)) > score(t + str(i)):
        ans += card[i] * (card[i] - 1)
n = 9 * k - 8
print(ans / n / (n - 1))
