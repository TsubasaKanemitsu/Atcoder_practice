# ABC 205 C
# 偶奇の場合分け(パリティ)

a, b, c = list(map(int, input().split()))

if c % 2 == 0:
    a = abs(a)
    b = abs(b)
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
else:
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
