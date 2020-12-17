## 文字列の順序入れ替え手法
```
s = list(input())

for i in range(len(s)):
    _s = s[i:] + s[0:i]
    print(result)

ex.
input -> abc
output -> [a, b, c], [b, c, a], [c, b, a]
```

## アルファベットの全列挙
```
alpabet = [chr(ord('a') + i) for i in range(26)]
```