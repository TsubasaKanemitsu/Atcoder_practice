from collections import Counter
s = input()

cnt = Counter(s)

if len(s) <= 2:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
else:
    for i in range(112, 1000, 8):
        # 共通部分を抽出した結果が8の倍数の集合と同じであるとき，8の倍数に並び変えることができる．
        if Counter(str(i)) & cnt == Counter(str(i)):
            print("Yes")
            exit()
    print("No")
