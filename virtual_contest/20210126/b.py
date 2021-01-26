a, b, x, y = list(map(int, input().split()))

if a == b or a == b + 1:
    print(x)
    exit()
elif a < b:
    kaidan = y * (b - a) + x
    rouka = x * ((b - a) * 2 + 1)
elif a > b:
    kaidan = y * (a - b - 1) + x
    rouka = x * ((a - b) * 2 - 1)

time = min(kaidan, rouka)
print(time)

# 考察
# 廊下で行く場合, 階段と廊下のみで行く場合，1回廊下渡るだけで行くパターンの3つの場合分けを行った．