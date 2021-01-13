# Atcoder問題傾向対策


## 入出力観点

## 文字列操作観点

## 演算観点
## 制御フロー観点

## 組み込み関数観点

## モジュール観点

## データ構造観点

## アルゴリズム観点

## 計算量観点

## 数学観点
### 88C(復習)
- 解答時間
    - 解けた(10分)
- パターン
    - 数列
- 考察
数列AはX以上Y以下の整数でAi+1はAiの倍数であり，Ai+1はAiより真に大きいという条件なのでAiがyを超えるまでAi = Ai-1 × 2を計算し続ければいい
(公式解答とは別の解き方である:公式の方がいいかも)
```
x, y = list(map(int, input().split()))

ans = [x]
count = 1
while True:
    temp_ans = ans[count - 1] * 2
    if temp_ans <= y:
        ans.append(temp_ans)
    else:
        break
    count += 1
print(len(ans))
```



## カテゴリ観点