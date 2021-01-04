stopper = '-'
result = []
while True:
    card = list(input())
    if "-" in card:
        break
    count = int(input())
    for k in range(count):
        h = int(input())
        extract_card = card[0:h]
        card = card[h:] + extract_card
    result.append(card)

for i in range(len(result)):
    print(''.join(result[i]))