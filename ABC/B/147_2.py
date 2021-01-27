# 7分30秒
s = input()

l = len(s)

if l % 2 == 0:
    s1 = s[0:int(l/2)]
    s2 = s[int(l/2):]
    s2 = s2[::-1]
else:
    s1 = s[0:int(l/2)]
    s2 = s[int(l//2 + 1):]
    s2 = s2[::-1]

count = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        count += 1
print(count)

# 考察(想定解とは異なる)
# 回文なので，二回目の文字列がどこから始まるのかを考える必要がある
# 元の文字列が奇数と偶数の場合で二回目の文字列の開始位置が変わることに注意して，
# 回文となるかを判定する要素である文字列を比較し異なる数をカウントする