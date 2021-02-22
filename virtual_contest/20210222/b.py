# コーナーケース
h, w = list(map(int, input().split()))

if h == 1 or w == 1:
    print(1)
    exit()

even_index = h // 2
if h % 2 == 0:
    odd_index = h // 2
else:
    odd_index = h // 2 + 1

even_col = w // 2
if w % 2 == 0:
    odd_col = w // 2
else:
    odd_col = w // 2 + 1
ans = odd_col * odd_index + even_index * even_col
print(ans)