N = int(input())
blue_card = []
for i in range(N):
    blue_card.append(input())

M = int(input())
red_card = []
for i in range(M):
    red_card.append(input())

ans = 0
card_list = list(set(blue_card))
for card in card_list:
    b_num = blue_card.count(card)
    r_num = red_card.count(card)
    ans = max(ans, b_num - r_num)
print(ans)

# 青の文字列が多く入っている要素を知りたい
# 青の文字列リストを取得し，青と赤にその文字列が何個ずつ入っているかを確認し，
# 計算することで差し引きの最大を求めることができる