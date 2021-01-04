have_card = int(input())
cards = []
for i in range(have_card):
    kind_card, num = list(input().split())
    num = int(num)
    if kind_card == 'S':
        cards.append(num)
    elif kind_card == 'H':
        num = num + 13
        cards.append(num)
    elif kind_card == 'C':
        num = num + 26
        cards.append(num)
    elif kind_card == 'D':
        num = num + 39
        cards.append(num)

for i in range(1, 53):
    if not(i in cards):
        if i >= 1 and i <= 13:
            print('S', i)
        if i >= 14 and i <= 26:
            print('H', i - 13)
        if i >= 27 and i <= 39:
            print('C', i - 26)
        if i >= 40 and i <= 52:
            print('D', i - 39)