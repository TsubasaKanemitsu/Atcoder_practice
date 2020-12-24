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

## 多重リストのソート
```
ans = sorted(ans, reverse=False, key=lambda x: x[1])

#昇順
input = [[2, 3], [1, 2], [3, 1]]
output = [[3, 1], [1, 2], [2, 3]]
```

## 順列
```
imort itertools
seq = [1, 2, 3]
perm = list(itertools.permutations(seq))

例
perm = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```