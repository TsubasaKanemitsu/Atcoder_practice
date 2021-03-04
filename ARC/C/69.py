# 貪欲法
# Sccを作成できるパターンを場合分けする
# S -> 1, c -> 2
# c -> 4
# 10分

s, c = list(map(int, input().split()))

if s >= c:
    print(c // 2)
else:
    c -= 2 * s
    c = c // 4
    print(s + c)