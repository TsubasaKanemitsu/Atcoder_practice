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
    - 復習1回目：解けなかった(始点，終点の扱いの判断ができていない, min, maxの条件を具体例から考える)
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
    - 復習(12分で解けた：数え上げの問題：全探索)
- 102
    - 4分
    - 貪欲法的な感じ?全探索で最大の差を求めると計算量的に時間内で解けない．そのため最大値と最小値を求めて最大の差を求める
- 103
    - 7分
    - 文字列の入れ替え(文字列の先頭を末尾につけていく)
- 104
    - 7分
    - 文字列の条件判定
- 107
    - 14分
    - 多重配列の操作系の問題
    - 白，黒をFalse, Trueで表してもいいかも
- 108(復習)
    - 33分
    - 図形の問題
    - 座標を具体的に書いてイメージする
    - しょうもないミスが多かった
    - 復習
    - 幾何問題(10分で解けた)
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
    - 復習
    - 数列問題(10分で解けた)

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
- 132
    - 3分半
    - 値の大小比較
- 133(復習必要)
    - 20分
    - 全探索
    - 条件をしっかり読む
    - 座標の全組み合わせで距離の計算を行い，求めた距離が整数であるかを判定し，整数である場合，+1 加算する
    - 復習完了〇
- 134
    - 10分
    - for文を0から始めていたため，条件の境界付近の値の判定を誤っていた.
- 135(復習必要かも?)
    - 25分
    - print文の認識間違えでミス
    - 数値の法則を見抜く必要がある
    - 復習完了〇
- 137
    - 22分
    - 条件指定で時間がかかった(問題文をちゃんと読むべきだった．考慮しなくていい条件について考えていた)
- 138
    - 4分
    - 分数の総和
- 139
    - 3分30秒
    - 文章から条件を考える

- 147(復習必要かも?)
- 11分
    - リストの始点・終点
    - 前と後ろから順に比較すればいい
    - リストの入れ替え処理はいらない
- 143
    - 3分30秒
    - 組み合わせ問題
    - 重複なしの全探索
- 145
    - 5分
- 146
    - 10分
    - アルファベットの数字化後の足し算で手間取った
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
- 128(復習)
    - 解けなかった
    - bit全探索
- 134(復習)    
    - 解けなかった
    - 計算時間を推測できていなかった
    - 最大Nが20万通りあって，それぞれで最大値を求めようとすると，20万×20万という膨大な計算量となる(4 × 10の4乗)そのため，計算量が減るように計算を行う必要がある．
- 138(復習)
    - 解けなかった
    - どの順番で値を更新していくことで，最大値を出力できるのかという観点での考察が抜けていた
- 139
    - 7分30秒
    - 2重ループを使用せずに，最大値を更新しながら処理を行うのが肝
    - 152の類題でもある?
- 141
    - 15分
    - 計算量を意識する必要がある
    - Kポイントから解答をミスした人を-1ずつ減点するのではなく，正解した人に加点していき，問題数分の減点を全員に与えることで正解数の差を付けることができる．これにより，大幅に計算回数を削減できる.
- 142
    - 多重リストのソート方法
    - 問題文の解釈のミス
- 143
    - 27分
    - 最後の隣接している文字列をどのように追加すべきか迷った
- 148
    - 9分
    - 最小公倍数を求める問題
    - 最小公倍数の基本問題
- 149
    - 15分
    - 素数判定を行う問題
    - 素数判定の基本問題
- 150
    - 9分
    - 順列の問題
    - itertools.permutaions
- 151(復習)
    - 35分(WA 5回)
    - 問題文をよく読むこと
    - WAのカウント方法を勘違いしていた。一度もACしていない問題に対するWAはカウントにいれない
    - 問題通りに実装する問題
- 152(復習)
    - 解けなかった
    - 問題文をよく読む
    - 高速化のために処理を軽くする
    - 範囲指定を行い，毎回最小値を見つけようとする処理がよくない. 最小値は更新すればいい
    - 139の類題でもある?
- 153
    - 4分30秒
    - 最小で済ませるために必要な方法を考える
    - 最大値から順番にリストから排除する
- 154
    - 2分30秒
    - 重複しているか否かの判定
- 155
    - 40分
    - 解けなかった
    - 計算量の見積方法がよくわからなかった
    - 辞書型の操作
- 156
    - 10分
    - for文の最大値に工夫を加えた
    - テストケースの想定が甘かった
- 157(復習)
    - 解けなかった
    - 全探索
    - -1となる条件の定義を考慮しれていなかった.
    - 考察力をつける. 例題の入力例をよく観察する

- 158
    - 11分
- 159(復習)
    - 解けなかった
    - 相加相乗平均の問題
- 160
    - 解けなかった
    - 問題の解釈の変換ができていない
    - 経路が最少になるとは，すなわちどういうことなのかを導き出す必要があった．
- 161
    - 21分 (1WA)
    - 最小値を考えるときに，最後に一回x - kを行うべきか否かを判定する処理をいれることでオーダを少なくしつつ処理することが可能になる．
- 162
    - 13分
    - 複数変数の最大公約数の総和
    - 3変数の最大公約数を求める場合の性質を知っておく必要がある．
- 163(復習)
    - 解けなかった
    - 問題文をよく読むこと

- 164
    - 2分30秒
    - setを用いる問題
    - 重複を含まない
- 166(復習?)
    - 40分
    - 解けなかった．計算量が収まらなかった
    - appendやremoveで条件に合う展望台の数を計算しようとする方法がよくなかった. オーダを大きくする処理にしている．
    - 条件に一致するかどうかをTrue, Falseで判定して，値の更新処理を行う方が処理が軽い．
- 168
    - 15分
    - 三角形の斜辺を求める問題
- 169(復習)
    - 解けなかった
    - 浮動小数点誤差に関する知識を問う問題
    - bをfloat型で受け取ってもその時点で誤差が生じている．そのため文字列としてbを受け取り，×100した分までの数値としてbを再定義(b = int(b[0] + b[2] + [3]))し, a * b // 100すればいい
- 170(復習)
    - 30分
    - 差の最少の数字を探索する方法の発想の転換が必要
    - 可変にする対象を入れ替えて考える
- 173(復習)
    - 解けなかった
    - bit全探索問題
    - 色の塗り方の全探索を行う
- 175
    - 解けなかった
    - 整数問題(剰余)
    - 距離に関する場合分けを言語化することができなかった
    - 図示して，場合分けパターンを考える必要がある．
- 176
    - 10分
    - 要素同士の比較
- 177(復習)
    - 累積和の問題
    - 35分
    - 累積和を用いることは分かっていたが，実装がうまくいかなかった．
    - O(N)とO(1)の考え方がイマイチ理解できていない
- 178
    - 解けなかった
    - 包除原理を思いつかなかった
- 179(復習)
    - 解けなかった
    - A * B + c = Nになるとは，すなわちどういうことなのか，解釈を変える必要がある．
    - 全探索では解けない
- 180(復習)
    - 9分
    - 約数列挙の問題
    - [約数列挙の解説](https://qiita.com/drken/items/a14e9af0ca2d857dad23)
- 181(復習)
    - 16分
    - 3点の座標が同一直線状に存在するかを判定する
    - 重複なし全探索 = 組み合わせ
    - qiitaの記事を参考
- 182
    - 解けなかった
    - bit全探索
    - 解法の足掛かりはつかめていたが，コードに落とし込むことができなかった
    - bit全探索で桁を消すパターンのbit全探索を行い，消す桁の数が少ない場合における残りの桁の総和が3の倍数であるかを判定する
- 183
    - 27分
    - 解けたが時間がかかった
    - 組み合わせ問題?
- 185(復習)
    - 解けなかった
    - 組み合わせの基本問題

## D問題
- 187
    - 解けなかった
    - 差分の考え方が思いつかなかった

