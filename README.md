# Atcoder_practice

## A問題
- 176
    - 問題を最後まで読み，条件を理解するべき
- 175
    - 場合分け
    - 全通り試せそうなパターンは全列挙する
- 168
    - 1の位を利用するために10で割った余りを求める方法がある
- 167(大事)
    - 双対問題
    - 与えられた文字列に1文字追加したもののが条件にあうかどうかは，追加後の状態を調べるのではなく，追加前に戻すと同じになるかを考えた方が良い.

- 159
    - 組み合わせの問題
    - 合計値が偶数になる組み合わせを求める

## B問題
- 66
    - 30分以上
    - rangeの逆順のループを使うべきだった
- 71
    - 3分半
    - アルファベットの全列挙
    - 文字列のソート

- 74
    - 7分
    - 問題の状況を理解するために図を思い浮かべる

- 79
    - 3分半
    - 数列の問題
    - i - 1, i - 2番目の値をどのようにループ内で確保していくかを考える必要があった.
- 82
    - 20分
    - 全探索(文字列ソートでも可能，むしろそっちの方が楽だった)
- 91
    - 7分
    - リスト操作(set, )
- 93(復習?)
    - 解けなかった
    - rangeの始点，終点の扱いの判断が遅い
    - 問題自体は難しくない
- 97
    - 20分
- 98
    - 14分
    - set()を用いた共通要素数の抽出
    - リストの操作
- 100(復習)
    - 解けなかった
    - 問題の要素を分解する
    - 数値の性質の考察が足りていない
- 103
    - 7分
    - 文字列の入れ替え(文字列の先頭を末尾につけていく)
- 104
    - 7分
    - 文字列の条件判定
- 108(復習)
    - 33分
    - 図形の問題
    - 座標を具体的に書いてイメージする
    - しょうもないミスが多かった
- 109
    - 8分45秒
    - 制約条件を満たすかどうかを検証する
    - 問題の分解
- 113
    - 8分
    - if文
    - 最適値の探索
- 114
    - 8分
    - リストと文字列の使い分け(len, スライスなど)

- 116(復習必要)
    - 数列の問題
    - 割り算 -> 小数点以下切り捨て

- 1117
    - 2分30秒
    - 総和，最大値の比較の問題

- 118
    - 8分
    - 共通項の抽出
    - list, set, &の練習になる

- 119
    - 5分
    - if文
    - 条件分岐と総和の問題

- 123(復習必要?)
    - 最後に注文するメニューを選ぶ方法を考える
    - 全探索 or 貪欲法?

- 128(復習必要)
    - 25分
    - 複数キーによるソート

- 133(復習必要)
    - 20分
    - 全探索
    - 条件をしっかり読む
    - 座標の全組み合わせで距離の計算を行い，求めた距離が整数であるかを判定し，整数である場合，+1 加算する

- 135(復習必要かも?)
    - 25分
    - print文の認識間違えでミス
    - 数値の法則を見抜く必要がある
- 139
    - 3分30秒
    - 文章から条件を考える

- 147(復習必要かも?)
- 11分
    - リストの始点・終点
    - 前と後ろから順に比較すればいい
    - リストの入れ替え処理はいらない
- 148
    - 2分
    - 文字列結合

- 149(復習)
    - 12分30秒
    - 貪欲法
    - 数直線を書いてイメージする
    - 計算量的にfor文が使えないことを認識する

- 151
    - 4分30秒
    - 出力に応じた条件の列挙
- 152
    - 1分30秒
    - 文字列の掛け算
- 153
    - 2分
    - リストの総和
- 154
    - 文字列の掛け算
    - 1分30秒
- 155
    - 整数の性質を問う問題(偶数の性質)
    - 4分30秒
- 156
    - 桁数カウント問題
    - 5分

- 157(復習)
    - 30分かかった
    - 多次元配列の扱い(慣れていない)

- 158(復習)
    - 15分かかった
    - 一回の操作でどのようにカウントできるかを考える．

- 159
    - リストのインデックスの始点，終点
- 160(復習)
    - 硬貨の枚数カウントをループで実現しようとしていた
    - 貪欲法
- 161(復習いらない)
    - list内包表記でリスト内の条件に一致する要素を抽出する

- 162(復習いらない)
    - 計算するための数値抽出方法の条件を，制約を元に考える(elseで表現していては，記述量が無駄に多くなる)
- 163(復習いらない)
    - 
- 164(復習いらない)
    - Yes, Noを表示する条件をきちんと読む
- 165
    - 割り算
    - 商の切り捨てについて知らなかった
    - / -> // (小数点以下切り捨て)

- 166(復習:15分)
    - リストの差分
    - 問題文の意図を読み解くのに時間がかかった

- 167(復習)
    - 貪欲法
    - 全探索ではない
    - 値を最大値にするために必要な条件を分解する
- 169(復習)
    - for文
    - 計算量を減らせる方法を考える

- 177(復習)
    - 文字列一致関係の問題(良問)

- 176(復習)
    - 各桁の和を用いる問題
    - python 3は多倍長整数で扱えるので，大きな数字をintとして受け取って計算が可能(メモリを好きなだけ使えるということ)
    - pythonはメモリ管理を意識させない仕様になっている

- 175(復習)
    - 三角形の条件
    - 全探索可能かどうか
    - for文の条件を制約から読み解く

- 174(復習いらない)
    - 簡単
    - if, for文

- 173(復習いらない)
    - 簡単
    - if, for文

- 172
    - sortして低い価格から要求された種類の果物の値段を加算することに気づけるかが肝

- 170
    - 鶴亀算
    - 全探索問題(復習する)

## B問題苦手な内容
- listやrangeの始点，終点の操作
- 全探索
- 多次元配列

## C問題
- 176
    - 10分
    - 要素同士の比較