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

## 累積和
累積和の前処理を事前に行うことで(O(N))，
区間の総和をO(1)で求めることができる．
```
num = list(map(int, input().split()))

cum_sum = [num[0]]

for i in range(1, len(num)):
    print(i)
    cum_sum.append(cum_sum[i - 1] + num[i])

print(cum_sum)
```