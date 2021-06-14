q = int(input())

card = []
ans = []
for i in range(q):
    t, x = list(map(int, input().split()))
    if t == 1:
        card.insert(0, x)
    elif t == 2:
        card.append(x)
    else:
        ans.append(card[x - 1])

for a in ans:
    print(a)
