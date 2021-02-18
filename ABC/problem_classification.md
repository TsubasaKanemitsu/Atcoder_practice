# Atcoder問題傾向対策


## 入出力観点

## 文字列操作観点
### 44B
- 解答時間 
    - 7分
- パターン 
    - 文字列カウント
- 考察
文字列中に存在する英子文字が偶数個ずつ存在するか確認すればいいので，
set()で一意な英子文字を抽出し，それらの英子文字が偶数個であるかを文字列に対してcountで求めその値を÷2し，その時の余りが0 or 1で偶数か奇数化を判定すればいい．

### 58C
- 解答時間
    - 7分
- パターン
    - 文字のカウント数
- 考察
この問題は，与えられた文字列群で共通に出現する文字列のみで構成しえる最大長の文字列を答える必要がある．
そのため，Counterで各文字列毎の文字数をカウントした集合を作成し，その集合が度の文字列をカウントした場合の集合とも共通であるようなカウントの集合を求める．最後に求まったカウントの集合のキーと値は共通で出現する文字列とその回数なので，その2つを利用して文字列を再構成し，再構成し得る文字列の中で最も辞書順で小さくなるようにソートすれば解を得ることができる．
### KEYENCE Programming Contest 2019 B (復習)
- 解答時間
    - 解けなかった
- パターン
    - 全探索，部分文字列
- 考察
連続した部分文字列を一度だけ取り除いた文字列がkeyenceに変換できるか判定する必要がある．
1. 文字数は最大で100文字なので，部分文字列を全通り試すことができる．
2. 全探索で，取り除く部分文字列を全通り試し，その結果がkeyenceと一致するかを判定すればいい．

## ARC 104 B (復習)
- 解答時間
    - 解けなかった
- パターン
    - 文字列操作，部分文字列の全探索
- 考察
この問題ではSの部分文字列の一部または全ての文字を入れ替えることで(A, T), (C, G)の対応関係(先頭からの文字数は同じとする)が成り立つ部分文字列は何個あるか求める問題である．
この問題では，全ての部分文字列を見ていく必要があるので，部分文字列の全探索を行う．
部分文字列中の文字を入れ替えることで対応関係を作ることができるのは，部分文字列の中の(A, T)と(C, G)のそれぞれの文字数が同じになっている必要がある．
文字数が同じであるかどうかを確認する方法は，部分文字列内を順にi ~ j番目まで走査する．(A, T), (C, G)のそれぞれの組み合わせの文字数が同じかを判断するカウンタ変数をcount1, count2とすると，A, Cが出たときは，count1とcount2を+1し，T, Gが出たときは，count1とcount2を-1する.j番目まで走査したときにcount1, count2が0になっていれば，その文字列は入れ替えることで問題文の条件を満たす文字列と判定する子tができるのでカウントされる．
このように解くことでO(N^2)で処理を行うことができる．
```
n, s = list(input().split())
n = int(n)
ans = 0
for i in range(n):
    count1 = 0
    count2 = 0
    for j in range(i, n):
        if s[j] == 'A':
            count1 += 1
        elif s[j] == 'T':
            count1 -= 1
        elif s[j] == 'C':
            count2 += 1
        elif s[j] == 'G':
            count2 -= 1
        if count1 == 0 and count2 == 0:
            ans += 1
print(ans)
```
### 137C
- 解答時間
    - 18分
- パターン
    - 文字列一致，計算量
- 考察
与えられた文字列がアナグラムになる組み合わせは何パターンあるかを求める問題
1. 同じ文字が複数回現れるとき，アナグラムとなるのである一方の文字列の各文字の出現回数ともう一方の文字列の各文字の出現回数が一致するかを比較すればいいが，この方法では計算量が膨大になるため，実装としては没となる．
2. アナグラムになるということは文字列をソートして並び変えたときにまったく同じ文字列になるということなので，与えられた文字列をソートする．
3. ソートした文字列をカウントし，2以上であるものは組み合わせを考えられるので，
カウント数 × (カウント数 - 1) / 2を2以上カウントされた回数にあてはめて計算することでアナグラムの組み合わせ数を求めることができる．
```
# 18分
from collections import defaultdict
from math import factorial


def combinations_count(n, r):
    import math
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))

n = int(input())
S = [''.join(sorted(list(input()))) for _ in range(n)]

cnt = defaultdict(int)
for s in S:
    cnt[s] += 1
ans = 0
for k, v in cnt.items():
    if v >= 2:
        ans += combinations_count(v, 2)
print(ans)
```
### AGC 6 A
- 解答時間
    - 40分
- パターン
    - 部分文字列比較
- 考察
文字列の一致パターンとして全文字一致，部分文字列一致，全不一致の3パターンにわけることができる．
1. 全文字一致は長さN
2. 全不一致の場合は2N
3. 部分文字列一致の場合は，sの先頭からi番目以降の文字列がtのi番目以前の文字列が一致するかを判別することでi番目までの一致しない文字列分と一致している文字列分を足した長さの3パターンで表現することができる．
```
n = int(input())
s = input()
t = input()

if s == t:
    print(len(s))
    exit()

match_cnt = 0
cnt = 0
for i in range(len(s)):
    for j in range(len(s) - i):
        if s[i + j] != t[j]:
            cnt += 1
            match_cnt = 0
            break
        else:
            match_cnt += 1
    if match_cnt == len(s) - i:
        break
ans = cnt + match_cnt + len(t) - match_cnt

print(ans)

# 他の解答でわかりやすいもの
# N = int(input())
# s = input()
# t = input()
# if s == t:
#     print(N)
#     exit()
# c = 0
# for i in range(N):
#     if s[i:] == t[:-i]:
#         c = i
#         break
# if c:
#     print(c + (N - c) + c)
# else:
#     print(N + N)
```
### 158D (復習)
- 解答時間
    - 解けなかった
    - 解法は大まかに思い浮かんでいた．
    - 解説AC
- パターン
    - deque()
- 考察
問題文通りの実装だと，t == 1のreverseにおいて文字数が多い場合にTLEになってしまう．
そこでt = 1のときに，reverseを行わずに文字列の先頭への追加と末尾への追加を正しく行う必要がある．
1. reverseが起きるたびに文字列の先頭と末尾が入れ替わるため，情報を持っておく必要があるため，t == 1のときに先頭と末尾の情報を更新する．
2. 先頭と末尾の情報を元に文字列への追加方法を適切に行う．appendleftとappendを先頭と末尾情報の条件によって使い分ける．
3. 最後にreverseが起きた回数が偶数回であれば，文字列の入れ替えを行わなくていいが，奇数回の場合はreverseを一回行う必要がある．
これらの処理により時間内で処理が終わる.  注意点として，文字列の追加はデータ構造をdequeにし，O(1)で追加処理を終わらせる必要がある．
'''
from collections import deque
s = deque(input())

Q = int(input())

st = 0
rev_cnt = 0
for i in range(Q):
    q = list(input().split())
    t = q[0]
    if t == '1':
        rev_cnt += 1
        if st == -1:
            st = 0
        else:
            st = -1
    elif t == '2':
        f = q[1]
        c = q[2]
        if f == '1':
            if st == 0:
                s.appendleft(c)
            else:
                s.append(c)
        elif f == '2':
            if st == 0:
                s.append(c)
            else:
                s.appendleft(c)
if rev_cnt % 2 == 1:
    s.reverse()
print(''.join(s))
'''
### 174D(復習)
- 解答時間
    - 解けなかった
- パターン
    - 文字列置き換え，入れ替え
- 考察
[参考の解答 & 考察](https://www.oyoshi.work/entry/abc174-ad-python/#DAlter_Altar)
- 感想
文字列操作の問題は条件にあった場合，最終的にどのような解になるのかをイメージする必要がある．
闇雲に条件にあてはめた操作を行うと，パターンを掴みづらくなる．
```
n = int(input())
c = list(input())

red_count = c.count('R')
ans = 0
for i in range(red_count):
    if c[i] == 'W':
        ans += 1
print(ans)
```
## CODEFESTIVAL 2017FINAL A (復習)
- 解答時間
    - 解けなかった
- パターン
    - 文字列正規表現
- 考察
与えられた文字列にAを追加してAKIHABARAを作ることができるかという問題なので，
AKIHABARAの中で4つのAがそれぞれある場合とない場合の全パターンの文字列の場合のみAKIHABARAを作ることができる．それらの文字列の全パターンを挙げるのはミスが出る可能性があるので，正規表現を用いて解答すればいい．
## 演算観点
### 64 C
- 解答時間
    - 20分
    - 2WA
- パターン
    - 場合分け
- 考察
色の種類数が最小になる場合と最大となる場合のパターンを考えなければならない．
1. 3200以上のレートの人がいる場合
3200以上のレートの人数分色が増やせるので最大数は最小数 + 3200以上のレートの人数となる．最小数は色が決まっている人のレート帯の種類と同じになる．
例外として，色が決まっているレート帯の人がいない場合は，最小数は3200以上のレート帯の人たちが同じ色を選ぶ必要があるため1種類となり，最大数は3200以上のレート帯の人たちがバラバラに色を選ぶことになるので，3200以上のレート帯の人数分となる．
2. 3200以上のレートの人がいない場合
最小数から色を増やす手段がないため最小数と最大数は色が決まっている人のレート帯の種類と同じになる．
### 65C 
- 解答時間
    - 17分
- パターン
    - 場合分け
- 考察
[参考](https://img.atcoder.jp/arc076/editorial.pdf)
```
# 22分
# 参考 https://img.atcoder.jp/arc076/editorial.pdf
n, m = list(map(int, input().split()))

def permutaions_count(n, r):
    import math
    return math.factorial(n) // math.factorial(n - r)

if abs(n - m) > 1:
    print(0)
    exit()
else:
    if n % 2 == 0 and m % 2 == 0:
        ans = 2 * permutaions_count(n, n) * permutaions_count(m, m) % (10 ** 9 + 7)
    elif n % 2 == 0 and m % 2 == 1:
        ans = permutaions_count(n, n) * permutaions_count(m, m) % (10 ** 9 + 7)
    elif n % 2 == 1 and m % 2 == 0:
        ans = permutaions_count(n, n) * permutaions_count(m, m) % (10 ** 9 + 7)
    elif n % 2 == 1 and m % 2 == 1:
        ans = 2 * permutaions_count(n, n) * permutaions_count(m, m) % (10 ** 9 + 7)
    print(ans)
```
### 94C (復習)
- 解答時間
    - 解けなかった
- パターン
    - ソート，問題理解
- 考察
[参考](https://qiita.com/hkrutknouch/items/220c158cb897762ac307)

### 81C
- 解答時間
    - 15分
- パターン
    - ソート，条件を満たす最小値を求める
- 考察
少なくとも何個のボールの整数を書き換える必要があるかと聞かれているのが，これは最小で何個の整数を置き換えると整数の種類がK種類になるのかと聞かれていることになるので以下の手順で考える．
1. 整数の種類とボールを書き替える個数が問題に関係するので，整数とその整数の個数が対応した辞書を作成し，種類の数と個数を求める．
2. 元の種類の数からK種類にするために置き換える必要がある整数を個数が少ない順に選んでいくことで置き換える必要がある整数の個数の最小値を求めることができる．
```from collections import Counter
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

A = Counter(A)
A = sorted(A.items(), key=lambda x: x[1], reverse=True)

num_kind = len(A)
ans = 0
i = 0
while k < num_kind:
    ans += A[i][1]
    num_kind -= 1
    i += 1
print(ans)
```
### 82C 
- 解答時間
    - 18分
    - 1WA
- パターン
    - ハッシュテーブル，条件
- 考察
与えられた数列の各数値と出現回数が一致させるために数列内の数値を取り除く操作回数の最小の値を求める．
1. 数値と出現回数をハッシュテーブルで作成する．
2. 数値と出現回数が一致しているかを判定し，一致しない場合は以下の2パターンの対処を行う．まず出現回数が数値より大きい場合は，取り除く回数は差分となる．出現回数が数値より小さい場合，出現回数を増やす操作はできないため，出現回数を0にする操作が必要となる．この2つの操作を与えられた数列に行うことで操作の最小回数が求まる．
```
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

ans = 0
for a in set(A):
    if cnt[a] >= a:
        ans += cnt[a] - a
    else:
        ans += cnt[a]
print(ans)
```
### 89C 
- 解答時間
    - 21分
- パターン
    - 場合分け，組み合わせ全探索
- 考察
制約として名前がM, A, R, C, Hから始まりかつ同じ文字から始まる人がいないという中での組み合わせを考える必要がある．
1. M, A, R, C, Hの中から3つの文字を選ぶ
2. 各文字の中の人から1人ずつ選ぶ
以上の2段階の組み合わせが存在する．
よって解法はMARCHで始まるそれぞれの人数を求め，1の組み合わせ×2の各文字あたりの人数(3人)をかけることで求めることができる．
```
# 21分
import itertools
n = int(input())

S = [input() for _ in range(n)]

m = len([s for s in S if s[0] == 'M'])
a = len([s for s in S if s[0] == 'A'])
r = len([s for s in S if s[0] == 'R'])
c = len([s for s in S if s[0] == 'C'])
h = len([s for s in S if s[0] == 'H'])

name = [m, a, r, c, h]
cnt = 0
for comb in itertools.combinations(name, 3):
    cnt += comb[0] * comb[1] * comb[2]
print(cnt)
```
### 116C (復習)
- 解答時間
    - 解けなかった
- パターン
    - 数え上げ
- 考察
[参考](https://drken1215.hatenablog.com/entry/2019/03/03/150200)
### 121C
- 解答時間
    - 解けなかった(復習はいらない，問題を解く方針は合っていた)
- パターン
    - 数え上げ
- 考察
最少の金額で栄養ドリンクを必要数購入する問題なので，
値段がもっと安い店舗で順に必要数に到達するまでドリンクを買い続ければいい
- ミスの要因
本数と値段の関係をdefaultdictで状態管理を行っていたが，なぜか値段を安くする順番にするソートが上手くいっていなかったため，計算結果が誤るテストパターンがあった．
defaultdictではなく，リストに変更するとACできた．
```
n, m = list(map(int, input().split()))
data = []
for i in range(n):
    a, b = list(map(int, input().split()))
    data.append((a, b))

data.sort()

money = 0
for i in data:
    if m >= i[1]:
        m -= i[1]
        money += i[0] * i[1]
    else:
        money += m * i[0]
        break
print(money)
```
### 117C
- 解答時間
    - 30分
    - 2WA
- パターン
    - 差分，ソート
- 考察
与えられた座標に最短で訪れるために必要な移動回数を求める．
1. n <= m, n < mで場合分けを考える使用可能なコマの数が移動すべき座標の数より多い場合，コマを座標に置くだけでいいので，行動回数が0となる．
2. n < mの場合，与えられた座標をソートし，最も近い座標間の距離を算出し，そのうち座標間の距離が大きい座標にコマを置く．移動回数としてはコマの数が足りない座標間の距離を移動回数とする．
以上より，最小の行動回数が求まる．
### 124C
- 解答時間
    - 解けた(10分)
- パターン
    - 数え上げ
- 考察
この問題では元の文字列のどの部分を変更することで隣同士の色を異なるようにすることができるかを調べたい．最少の変更回数を求めたい．
隣同士が異なる色のパターンは白黒白か黒白黒の2パターンなのでこの2パターンのうちどちらのパターンが元の文字列のパターンと近いかを調べれば最少回数で隣同士の色を異なるようにすることができると言える．
```
s = input()

odd = ''
even = ''
odd_count = 0
even_count = 0
for i in range(len(s)):
    if i % 2 == 0:
        odd = '0'
        even = '1'
    else:
        odd = '1'
        even = '0'

    if odd != s[i]:
        odd_count += 1
    elif even != s[i]:
        even_count += 1

print(min(odd_count, even_count))
```
### 127C
- 解答時間
    - 解けた(19分)
- パターン
    - 数え上げ
- 考察
ゲートを全て通ることのできる整数の数を求めることを考えればいい．
全てのゲートを介していくうちに下限と上限が徐々に狭まっていくので，狭まっていく下限と上限を更新しつづけ,最終的な下限の状態と上限の状態を管理し，
最後にその範囲の整数の数をカウントすればいい．
```
n, m = list(map(int, input().split()))

L, R = [], []

for i in range(m):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

low = L[0]
high = R[0]

for i in range(1, m):
    if low < L[i]:
        low = L[i]
    else:
        pass
    if high > R[i]:
        high = R[i]
    else:
        pass
   
num = [i for i in range(low, high + 1)]
print(len(num))
```
### 131D
- 解答時間
    - 15分
- パターン
    - 累積和、ソート
- 考察
時間内で仕事を終わらせられるかどうかを考える必要がある．
1. 早く終わらせるべき仕事順にソートする
2. 仕事を順番にこなしていった場合の累積の仕事時間を算出する
3. 累積の仕事時間が各仕事の求められている期限の時間より小さければ，仕事を完了することができる．大きければ，仕事を完了することができない．
```
n = int(input())
work = []
a = []
b = []

for i in range(n):
    _a, _b = list(map(int, input().split()))
    work.append([_a, _b])
    
work = sorted(work, key=lambda x: x[1])

time = 0
for i in range(len(work)):
    time += work[i][0]
    if time > work[i][1]:
        print("No")
        exit()
print("Yes")
```
### 132C
- 解答時間
    - 解けた(12分)
- パターン
    - 数え上げ
- 考察
ABCとARCの問題に分類される数が同じになるということは，問題の難易度が順番に並べられたときに半分の位置にくる数値がABCとARCの境界に関わる数値となる．よって半分に分割できる数値のパターンは半分の位置の数値とその1つ手前数値の間でとれる整数全てということになる．
```
k = int(input())

D = list(map(int, input().split()))
D.sort()
mid_num = D[k // 2]
mid_prev_num = D[k // 2 - 1]
num = [i for i in range(mid_prev_num + 1, mid_num + 1)]
print(len(num))
```
### 133B
- 解答時間
    - 15分
- パターン
    - 全探索
- 考察
与えられたXを用いて距離を求める全パターンを網羅するには，自分と自分以外の行全てのX同士を計算させる必要があるのでi ~ n, j = i + 1 ~ nの2重ループでその組み合わせは網羅することができる．更に列単位で距離計算を行っていくので, k ~ dのループが必要になる．これらの3重ループの全探索で距離を求め，距離の整数判定処理を追加することで問題を解くことができる．
- 備考
pythonでは整数判定のために，is_interger()という関数が使用できる．
```
# 15分
n, d = list(map(int, input().split()))

x = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i + 1, n):
        dis = 0
        for k in range(d):
            dis += abs(x[i][k] - x[j][k]) ** 2
        dis = dis ** 0.5
        if dis.is_integer():
            count += 1
print(count)
```
### 135 B
- 解答時間
    - 7分
- パターン
    - ソート
- 考察
与えられた数列が1回の入れ替え操作で昇順にできるかを判定する必要がある．
ということは，理想の昇順な数列と差異のある要素数は0か2であると考えることができる．よって，pと理想の昇順配列の要素が異なる数分カウントすることで解答を得ることができる．
```
n = int(input())
p = list(map(int, input().split()))

ans = sorted(p)

count = 0
for i in range(n):
    if p[i] != ans[i]:
        count += 1

if count == 0 or count == 2:
    print("YES")
else:
    print("NO")
```
### 135C
- 解答時間
    - 解けた(19分)
- パターン
    - 数え上げ
- 考察
勇者は，i, i + 1番目の町を襲っているモンスターを倒すことができるので，BiがAiより大きい場合，その差分の分だけ次の町のモンスターを倒すことができる．よって，合計値はA[i] + diff(B[i] - A[i])ずつ足していくことで倒したモンスターの数をカウントできる．注意すべき点は，勇者(Bi)がi番目の町にいるモンスターより多くモンスターを倒すことができる場合，A[i + 1]の値を更新することができる．そのときにBiのモンスターを倒せる数がB[i] > A[i] + A[i + 1]の状況でdiff(B[i] - A[i])分をA[i + 1]から減らすとA[i + 1]のモンスターの数がマイナスになってしまうので，diffは最大でもA[i + 1]までにしかならないようにする必要がある．
```
n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_val = 0
for i in range(n):

    if A[i] >= B[i]:
        sum_val += B[i]
    elif B[i] > A[i]:
        diff = B[i] - A[i]
        
        if diff > A[i + 1]:
            diff = A[i + 1]
        sum_val += A[i] + diff
        A[i + 1] = A[i + 1] - diff
    
print(sum_val)
```
### 139D
- 解答時間
    - 解けた(10分)
- パターン
    - 余りの累積和
- 考察
この問題で条件が与えられた各項の余りが最大となるのは，各項より1つ大きい値でそれぞれの項が割られると商が0, 余りが項のままとなり余りが最大値をとることになる．
結果的に最も値の大きい項は自分より1大きい値がないので必然的に割る数は1となり，余りは0となる．そのため，余りの総和の最大値は (1 mod 2) + (2 mod 3) + ... (n - 1 mod n) + (n mod 1)となる．ここでNは10の9乗のため，全ての項に対して演算を行うと計算時間が間に合わない(O(N)かかる)ため，累積和の公式を使う. n(n + 1)/2で1 + ... + Nまでの総和が表せることを利用することでO(1)で計算結果を出せることができる
```
n = int(input())

ans = n * (n - 1) // 2
print(ans)
```
### 165C
- 解答時間
    - 12分
- パターン
    - 場合分け, 関数の性質(単調増加)
- 考察
[参考](https://img.atcoder.jp/abc165/editorial.pdf)
- 感想
最大数ということを意識できていなかったので反省
どのようにxをとれば，floor(Ax/B), A × floor(x/B)のそれぞれの関数が最大化，最小化されるのか考えるべき．
### 166D
- 解答時間
    - 20分
- パターン
    - 全探索(探索範囲は制約条件から導き出す)
- 考察
a ** 5 - b ** 5が x(<= 10 ** 9) となりうるような範囲で全探索を行う必要がある．
1 ~ 10 ** 9 の範囲を全探索していては，計算量が間に合わないので，間に合うようにするために探索範囲を絞り込む必要がある．
a ** 5 - b ** 5でaとbの差が1異なるだけで値が10 ** 9を超えるような限界を導き出し，1異なるだけで差が10 ** 9になるのだからそれ以上の範囲は探索する必要がないと考えることができる．そうすることで全探索範囲を絞り込めて，計算時間内で処理を完了させることができた．
[参考](https://drken1215.hatenablog.com/entry/2020/06/20/231600)
- 感想
この手の問題は，愚直に全探索は無理なので，範囲を絞り込むために，範囲の下限と上限を推測するために具体的な数値を入れてみて考えるのが良い．
```
# https://mathtrain.jp/factorization2
# 20分
# 正当な解法ではない
# A, Bのとりうる最大値がわからなかったので無理やり因数分解の式から求めた
x = int(input())

for a in range(- 300, 300):
    for b in range(-300, 300):
        if a != 0 or b != 0:
            ans = (a - b) * (a ** 4 + a ** 3 * b + a ** 2 * b ** 2 + a * b ** 3 + b ** 4)
            if ans == x:
                print(a, b)
                exit()
```
### 171D
- 解答時間
    - 20分
- パターン
     - 差分更新(数え上げ関係?)
     - 159Dと同じ問題の部類らしい
- 考察
問題通りにAの中からBに該当する数値をCに置換するという操作し，その時の総和を求めるとなるとO(N^2)になるのでこの方法では無理なことがわかる．
1. 事前にAの中で出た数値の回数をカウントした辞書を用意する
2. Aの総和を計算しておく
3. B, Cが入力されるたびに1で作成した辞書のカウント回数を更新し，更新に応じて生じた総和の差を2で求めた総和を用いて算出し，操作毎に総和をdpに保持する
4. dpに操作毎の総和が保持されているので，それを表示する.
よってこれらの処理はO(N + Q)で完了する．
```
from collections import Counter
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
q = int(input())

sum_a = sum(a)
dict_a = defaultdict(int)
for i in a:
    dict_a[i] += 1
dp = []

for i in range(q):
    b, c = list(map(int, input().split()))
    num_b = dict_a[b]
    dict_a[c] += num_b
    dict_a[b] = 0
    sum_a += num_b * (c - b)
    dp.append(sum_a)

for i in range(q):
    print(dp[i])
```
### 181D (復習)
- 解答時間
    - 解けなかった
    - 解法は思い浮かんでいたが，実装できなかった
- 考察
※8の倍数であるかどうかは数値の下3桁が8で割り切れるかを判定すればいい．
与えられた数字列から3つの数字を選び出す組み合わせすべてを8で割り切れるかどうかを判定する方法が最初に思い浮かぶが，計算的に全探索は不可能である．

場合分けを考える．
1. 与えられた数字列が1, 2桁の場合は計算量が少ないため8で割り切れるかを全通りで試す．
2. 3桁以上の場合は，元々与えられた数字列の数字毎の出現回数の辞書を作成し，112 ~ 1000の間に現れる8の倍数の各桁の数字の出現回数の辞書と比較し，出現回数が同じであれば数字列を並び変えることで8で割り切れるかどうかを判定できる．
```
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
        if not Counter(str(i)) - cnt:
            print("Yes")
            exit()
    print("No")

```
### diverta 2019  Programming Contest B
- 解答時間
    - 10分
- パターン
    - 全探索
- 考察
r, g, bの箱数×玉の数の3重ループの全探索だと計算量的に間に合わないので，2重ループの全探索に工夫を行う必要がある．
r,g,bのうち2種類の玉数が決まれば，合計でN個となるために必要な残り1種類の玉の数はO(1)で決めることができる．そうすることでO(N^2)で全探索を行い，所望の組み合わせを求めることができる．
またfor分の各色に対する上限の設定方法は，1種類の箱だけ買う場合を想定し，玉の数の合計がNになる箱数なのでn // r, n // g, n // bなどと表すことができる．
```
r, g, b, n = list(map(int, input().split()))

cnt = 0
for i in range(n // r + 1):
    for j in range(n // g + 1):
        hako = n - r * i - g * j
        k = hako / b
        if k >= 0 and k.is_integer() and r * i + g * j + k * b == n:
            cnt += 1
print(cnt)
```
### みんなのプロコン C(When I hit my pocket) (復習)
- 解答時間
    - 解けなかった
    - 解法の方針は大まかに合っていた
- パターン
    - 場合分け, 貪欲法, O(1)の最適化問題
- 考察
[参考](https://drken1215.hatenablog.com/entry/2019/05/13/125000)
## 制御フロー観点
### 63C(復習必要)
- 解答時間
    - 30分(ほぼ溶けたようなもの)
- パターン
    - ソート
- 考察
与えられた数値の総和が10の倍数にならないような値の最大値の組み合わせを考える．
まずは，元の数値の総和が10の倍数であるかどうかを確認する．
10の倍数でなければ，それが最大値となるので出力する．
10の倍数だった場合は，総和から与えられた数値の小さいものから順に引いていき，10の倍数でなくなったタイミングの数値が最大値となる．
### 65C
- 解答時間
    - 20分
    - WA 3回
- パターン
    - 添え字と要素の値を用いたループ
- 考察
ボタン2が光っている状態かそれ以外かで出力値を変える．
そのために，それ以外の状態をどのように定義する必要があるのかを考えた．
N個のボタンがあり，それを条件通りに順番に押した場合，ボタン2が光るまでに押さなければならない最大の回数はN回である．そのため，N回ループを回し，ボタン2が光るとき以外は-1を出力するようにした．その結果，ボタンを押す指定条件がループした場合でも無限回押す必要がなくなる．また今回の条件ではNは最大で10の5乗だったので全探索が可能だったのでこの方法を採用した．
- 感想
時間がかかった理由は，添え字と要素の数値が問題文上で与えられている意味との対応付けがうまくできていなかった．ボタンiという表現とボタンaiという表現に混乱していた．

### ARC C 73
- 解答時間
    - 40分
- パターン
    - 配列操作，差分
- 考察
この問題では，スイッチを押すとT秒間お湯が流れるがお湯の出る時間が加算されていくわけではない．
1. T秒間は必ずお湯は流れる(最後にスイッチを押す人がいるから)
2. 最後にお湯がT秒間流れるということは，それまでに流れるお湯の時間については以下ように考えればいい．
3. i人目とi + 1人目のスイッチを押すまでの空き時間がT秒より長い場合，お湯の流れ時間はT秒
4. i人目とi + 1人目のスイッチを押すまでの空き時間がT秒より短い場合，お湯の流れ時間は空き時間分の秒数(重なり部分は次のスイッチを押す人の順番の時に秒数が加算されるため)
```
n, T = list(map(int, input().split()))
t = list(map(int, input().split()))

diff = []
for i in range(1, n):
    diff.append(t[i] - t[i - 1])

ans = 0
for i in range(n - 1):
    if T > diff[i]:
        ans += diff[i]
    else:
        ans += T
        
ans += T
print(ans)
```

### 86C.py
- 解答時間
    - 解けた(25分)
    - WA 2回
    - テストケースが1つだけ通らなくて, 時間を浪費した
- パターン
    - 座標移動
- 考察
制約として時刻t -> t + 1毎に必ずx座標かy座標をを +1 or -1 する必要がある．そのためその場にとどまることが許されない状態で移動可能かどうかを判定する方法として移動不可能なパターンとして以下の2点を考えた．1点目は，時刻tから次の時刻の移動可能距離(diff_t)がx, y座標それぞれの次の座標までの移動距離の総和(diff = diff_x + diff_y)より小さいときは移動が不可能であると考える．2点目は，移動可能距離から移動距離を引いた値(diff_t - diff)が偶数でないときは，移動不可能と判定する．これはなぜかというと移動可能距離が移動距離より大きいということは制限時間内に移動すべき位置へ行く時間は足りているので，あとはその場にとどまるための移動を行えばいい．移動時間が偶数の場合は，進んで戻るという行為が行えるが奇数の場合は進んだものの戻ることができないためとどまる行動ができたいという風に考えることができる．
```
n = int(input())

result = "Yes"
temp_x = 0
temp_y = 0
temp_t = 0
for i in range(n):
    t, x, y = list(map(int, input().split()))
    diff_x = abs(x - temp_x)
    diff_y = abs(y - temp_y)
    diff_t = t - temp_t
    diff = diff_x + diff_y

    if diff_t >= diff and (diff_t - diff) % 2 == 0:
        pass
    else:
        result = "No"
    temp_x = x
    temp_y = y
    temp_t = t

print(result)
```
### 87C
- 解答時間
    - 解答できた(25分)
    - 足し合わせ方法を具体的に書かなかったのが，遅かった原因
- パターン
    - 足し算
    - 全探索
- 考察
この問題は右か下にしか移動できないので一度2段目に下りると上がることはできなくなる．
そのため，キャンディーを拾える方法はある地点まで右に移動したときに拾ったキャンディの数と，2段目に下りてから右に移動したときに拾ったキャンディの数をあるルートで移動した場合に拾えるキャンディの総和と考える．そう考えると1ずつ右に移動して，そこから下に下りて右に移動するというルートの全探索を行い，最大で拾えるキャンディの数を更新し続ければいい．
```
n = int(input())

A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))

ans = 0
for i in range(n):
    temp_ans = sum(A_1[0:i + 1]) + sum(A_2[i:])
    ans = max(ans, temp_ans)
print(ans)
```

### 120C(復習)
- 解答時間
    - 解答できなかった
- パターン
    - 文字列検索
- 原因
0と1が隣あっているかどうかを配列同士の比較を行い判定していたため，
計算時間がかかりすぎていた．
- 考察
単純に考えれば，0と1が隣あったときにブロックを消すので，0と1の最小の数に合わせた分だけブロックを消すことができる最大の回数であるとわかる．
### 136C
- 解答時間
    - 解けた(10分)
- 考察
単調増加するビルの条件として右隣のビルの高さが自分と同じか自分より低いまたは1だけ低くする操作をした場合に同じ高さにすることができるという条件が
全ての位置のビルにおいて成り立つかどうかを検証すればいい．
また，別の解答として対象のビルに対して右隣のビルが2以上高い場合はNoという方法も考えられる．
(単調減少し続けているかを判断する)
- 解答
```
n = int(input())

H = list(map(int, input().split()))
H.reverse()
for i in range(n - 1):
    if H[i] >= H[i + 1]:
        continue
    else:
        H[i + 1] = H[i + 1] - 1
        if H[i] >= H[i + 1]:
            continue
        else:
            print("No")
            exit(0)
print("Yes")
```
### 185D(復習)
- 解答時間
    - 解けなかったが解き方の方向性は合っていた．
- パターン
    - ソート，差分の最小値
- 考察
1. 幅Kの決定方法
白色のマスが全部赤色になるように固定幅Kの赤スタンプを押す必要があるので，まずは青マス間の白マスが何個ずつ隣接して存在するのかを調べ，それらのうちの最小幅に合わせてKを設定する必要がある．
2. スタンプの押す回数
スタンプの押す回数は隣接している白マスの数 ÷ 幅Kで割ったときの商の切り上げた(押す回数は最小の整数なため)回数の総和となる．
## 組み込み関数観点
### 45B
- 解答時間
    - 10分
- パターン
    - pop
- 考察
現在のカードを見て，カードに該当する持ち手の手札を捨てさせるループをpopを利用して実装するだけ．

## モジュール観点
### 79C
- 解答時間
    - 解けた(20分)
- 全探索
    - itertoolsを使えばすぐできる
- 考察
4つの数字を+, -の演算を用いて7になる場合の数式と答えを出力すればいいので，
全パターンの計算を試し，答えが7になるときの数式と答えを出力すればいい
- 感想
文字列の足し算などで凡ミスをしてしまい解答に時間がかかってしまった
解き方の方針自体はすぐに出た．
```
import itertools
num = list(map(int, input()))

for perm in itertools.product(['+', '-'], repeat=3):
    flag = False
    ans = num[0]
    str_ans = str(num[0])
    for index, p in enumerate(perm):
        if p == '+':
            ans += num[index + 1]
            str_ans += p + str(num[index + 1])
        else:
            ans -= num[index + 1]
            str_ans += p + str(num[index + 1])
    if ans == 7:
        print(f'{str_ans}={ans}')
        flag = True
        break
    if flag:
        break
```
## データ構造観点
- 解答時間
    - 解けた(25分)
    - 3WA
- 考察
考察1
ai対して+1, そのまま, -1の操作のいずれかを行い，その処理後の数値の出現回数の最大値を求める必要がある．
全ての操作を行った後の数値を全列挙し，それぞれの数値が何回ずつ出現するかをカウントする方法では計算量がオーバーしてしまいWAとなった．
考察2
出現数数値と回数がわかれば，すぐに最大出現回数を求められるので，辞書型でkeyを処理後の値，valueを出現回数として持つことで，処理後の数値の出現回数のカウントをO(1)で行うことができるため，ACできた．
最初からハッシュテーブルを使用するべきであった．
※備考
collectionsというライブラリを用いれば，リスト内の要素の出現回数がオブジェクト型で持つことができるみたい．
```
from collections import defaultdict
n = int(input())
N = list(map(int, input().split()))

for i in range(n):
    N.append(N[i] + 1)
    N.append(N[i] - 1)

d = defaultdict(int)
for num in N:
    d[num] += 1

print(max(list(d.values())))
```
## アルゴリズム観点
### 66C
- 解答時間
    - 25分
- パターン
    - データ構造: deque()
- 考察
制約条件的にaのi番目の要素をbの末尾に追加し，逆向きに並べ替えるという操作をn回行うのは，O(N^2)になるため計算量的に処理できないことがわかる．
その次に考えられるのは，末尾に追加し，逆向きにするという部分でこの操作を先頭から追加に置き換えられないかと考えた．あとは具体例を参考に，nの偶奇とi番目の要素の偶奇を考慮し，条件を設定して，先頭から入れる要素と末尾から入れる要素を考えれば，O(N)で問題文通りの操作を行うことができる．
```
# 26分
from collections import deque
n = int(input())
a = list(map(int, input().split()))

ans = deque()

for i in range(n):
    if i % 2 == (n - 1) % 2:
        ans.appendleft(a[i])
    else:
        ans.append(a[i])

for i in ans:
    print(i, '', end='')

```
### 68C (復習?)
- 解答時間
    - 40分
- パターン
    - ハッシュ，グラフ系
- 考察
1. 開始位置と終了位置の関係をハッシュマップで定義する．
そうすることで終了地点⇒次の開始地点⇒終了地点⇒という風に位置を移動することができる．
2. 1つの開始位置から複数種類の終了地点到達する可能性もあるので，ハッシュテーブルとして値をもつときに，リスト型にする必要がある．
3. 今回は2回の定期便の移動で目的地にたどり着けるかを聞かれているので，1回目に乗った定期便の終了地点を開始位置として，終了地点を取得し(複数の場合あり),
その終了地点の中に目的値が入っていれば，到達可能である．
```
from collections import defaultdict
n, m = list(map(int, input().split()))
_bin = defaultdict(list)

for i in range(m):
    a, b = list(map(int, input().split()))
    _bin[a].append(b)

st = _bin[1]
for s in st:
    if n in _bin[s]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
``` 

### 77C (復習)
- 解答時間
    - 解けなかった
- パターン
    - 二分探索
- 考察
A < B < Cになるようなパーツの組み合わせの総和を求める必要がある．
真ん中のBを固定して，B以下となるAの数とB以上となるCの数を掛け算すれば，A < B < Cとなるパーツの組み合わせがわかる．
知る必要があるのは，Bに近いAの最大値が先頭から何番目であるのか?Bに近いCの最小値が先頭から何番目であるのかがわかれば，B以下のAの数とB以上のCの数がわかる．これを知るために，二分探索を利用したbisectというライブラリを使う．これは，与えられたターゲットを対象のリストの中に入れるなら何番目に入れることが可能なのかを返してくれる．bisectにより，知りたかった，B以下のAの個数とB以上のCの数を知ることができる．
```
# bisect (二分探索)
import bisect

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
lc = len(C)

ans = 0
for b in B:
    a = bisect.bisect_left(A, b)
    c = bisect.bisect_right(C, b)
    ans += a * (lc - c)
print(ans)
```
### DISCO presets ディスカバリーチャンネルコードコンテスト2020予選(B問題) (復習)
- 解答時間
    - 解けなかった
    - 惜しかった
- パターン
    - 累積和
- 感想
累積和を用いるところまでは分かっていたが，累積和を用いて2分割しながら左右の差の最小値を求めるという部分まで発想が至らなかった．
### 57B
- 解答時間
    - 10分
- パターン
    - 全探索
- 考察
各学生の位置から最も近いチェックポイントがどこであるのかを調べればいいので，
全探索で各学生ごとに全てのチェックポイントまでの距離を計算し，最短距離であるチェックポイントを選ぶようにすればいい．

### AGC 29 A (復習)
- 解答時間
    - 45分(2WA)
- パターン
    - 累積和
- 考察
この問題は'BW'となっている並びを'WB'に入れ替える操作を何回できるかを問いている．最終的な状態としてWWWBBBのように左側にWが集まり右側にBBBが集まる状態になることを想像できればいい．
操作回数の考え方は，各Wより左側にあるBの数だけ各Wは'BW'から'WB'に入れ替えることができると考えられるため，各Wの地点での累積のBの数がわかっていればいい．
そのため以下の処理を行う．
1. Bの数を累積和で数えるため，文字がBの場合は+1, Wの場合は現状維持となるように累積和をO(N)で求める．
2. その後，Wの部分での値を全て加算すれば，操作回数をO(N)で求めることができる．
```
# 2WA
# 45分
s = input()

cum_sum_b = [0 for _ in range(len(s) + 1)]
for i in range(1, len(s) + 1):
    if s[i - 1] == 'B':
        cum_sum_b[i]  = (cum_sum_b[i - 1] + 1)
    else:
        cum_sum_b[i] = cum_sum_b[i - 1]
ans = 0
for i in range(1, len(cum_sum_b)):
    if s[i - 1] == 'W':
        ans += cum_sum_b[i]
print(ans)

```
### ARC 109B (復習)
- 解答時間
    - 80分
- パターン
    - 二分探索
- 考察
長さ1からn + 1種類までの丸太から最小の本数で長さ1からnの丸太を1本ずつ作りたい．
ということは，1 ~ n + 1の中から長い方から順に選んでいき，1からnの長さの合計を超えたところで選ぶ本数は終了という風に考えることができる．
これをfor文でn+1から1ずつ減らしたものを加算していくのが最も単純な実装であるが，これは，O(N)であるため計算時間内に終わることができない．
次に考える方法が二分探索を用いたものである．
1 ~ n + 1の範囲で二分探索を行い，midからn + 1までの長さの総和が1 ~ nの総和と一番近くなるまで二分探索を続ける．
最後のmidの値とn + 1の差分が1~nの長さを実現するのに必要となる最小の本数となる．
```
n = int(input())

left = 1
right = n + 1

def binary_search(left, right, n):
    sum_val = (n * (n + 1)) // 2
    while right - left > 1:
        mid = left + (right - left) // 2
        # 区間和
        w_sum = (n * (n + 1)) // 2 - (mid * (mid + 1)) // 2
        num = w_sum + n + 1
        if num >= sum_val:
            left = mid
        else:
            right = mid
    return left

right = binary_search(left, right, n)
count = n + 1 - right
print(count)
```
### 122C
- 解答時間
    - 20分
    - 復習必要かも
- パターン
    - 累積和
- 考察
与えられた文字列の部分文字列としてACが何回現れるかという問題なので，制約がゆるければ，全探索でACの個数をカウントして解くことができるが，今回は制約上無理なので全探索はあきらめる．
次に考えたのが，O(N)の間にACの個数を数える方法である．
ACはiとi+1番目の文字列がACとなっている場合に+1とカウントされるべきであり，
それをn - 1番目その判定を行い，ACのカウント数を累積和の配列として持つ．
あとは指定区間内の最初と最後の累積和の引き算を行えば，指定区間ごとにO(1)で指定区間内におけるAC数を求めることができる．
- 感想
想定解答よりややこしいので，復習した方がいい
```
# 29分
# 1WA
n, q = list(map(int, input().split()))
s = input()
l = []
r = []
for i in range(q):
    _l, _r = list(map(int, input().split()))
    l.append(_l)
    r.append(_r)

count_list = [0 for i in range(n)]
count = 0
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        count_list[i] = count
        count += 1
        count_list[i + 1] = count
    else:
        count_list[i] = count
        count_list[i + 1] = count
# print(count_list)

for i in range(q):
    print(count_list[r[i] - 1] - count_list[l[i] - 1])

```
### 143D (復習)
- 解答時間
    - 解けなかった
- パターン
    - 2分探索
- 考察
[参考](https://img.atcoder.jp/abc143/editorial.pdf)
### 154D(復習)
- 解答時間
    - 解けなかった
    - 解説見た後は20分
- パターン
    - 累積和
- 考察
隣接するK個のサイコロの出る目の合計の期待値の全パターンを求めてから，最大値を求める方法では，O(NK)になるので時間内に処理が終わらない．
そこで各サイコロの出る目の期待値の累積和を計算し(O(N))，i + k番目の累積和からi番目の累積和を引くことで隣接するK個の期待値を算出できる(O(1))．それを全パターン調べるのにかかるオーダはO(N - K)なので時間内に処理を終えることができる．
### 144C
- 解答時間
    - 解けた(10分)
- パターン
    - 約数列挙の応用
- 考察
(1, 1)から(a, b)に至るまでの移動回数はa + b -2となる．
a, bを求めるとき，全探索をしていては計算時間内に処理を終わらせることができないので計算量を減らす方法を考える必要がある．
そこで，a, bはNを割ったときの数と商の組み合わせで求め，更にa≤bの対称性を用いることで計算量をO(N)からO(√N)に減らすように実装する．
```
n = int(input())

def get_max_div_mod(n):
    itr = 1
    result = [1, 1]
    while itr * itr <= n:
        if n % itr == 0:
            result = [itr, n // itr]
        itr += 1
       
    return result

result = get_max_div_mod(n)

print(sum(result) - 2)  
```
### 146C (復習)
- 解答時間
    - 解答できなかった
- パターン
    - 二分探索
- 考察
1 ~ 10^9でA × N + B × d(N)を満たすようなNを求める必要がある．
for文で探索していては，処理が間に合わない．
広い範囲の数値で用意されたターゲットの数値がある場合，ターゲットを基準に二分探索を行い，所望の数値を求めればいい．
### 167C
- 解答時間
    - 22分
- パターン
    - bit全探索
- 考察
この問題では，m個のアルゴリズムの理解度をx以上にするかつ参考書の購入料金を最小でにするような参考書の購入パターンを計算する必要がある．
1. 探索方法の方針としては，N個の参考書をそれぞれ買う/買わないの二通りで考え，それらの全ての組み合わせを考える. (bit全探索)
2. あとは，1の参考書の組み合わせで提供するアルゴリズムの理解度がx以上になるような時の料金を算出し，最小値で更新していけばいいことがわかる．
理解度がx以下になるときは，-1にすればいい

### CODE FESTIVAL 2017 qualC B
- 解答時間
    - 25分
- パターン
    - bit全探索，貪欲法
- 考察
bit全探索で解いた．
今回の問題では，与えられたAに対して(Ai = xiと考える)|xi - yi| ≤ 1となるようなb1, b2,..., bnの積が偶数になる組み合わせの数を考える．
|xi - yi| ≤ 1の条件を満たすbiにするには，aiに対してbi = ai + 1, ai, ai - 1が考えられるので，以下の処理を行う．
1. ai + 1, ai, ai - 1の三種類のリストの作成
2. 全組み合わせをitertoolsで求める．3^n個の組み合わせを求める．
3. 組み合わせの数値の掛け算の結果が偶数であるかを判定し，偶数であればカウントする．このようにすることでb1*b2*....bnが偶数となる組み合わせの個数を数えることができる．
(別解)
全ての組み合わせ数からb1*b2*...bnの掛け算の結果が奇数になる場合を差し引いた分が偶数の数になるという考え方．O(N)で求められる．<br>
考え方<br>
1. aiが偶数の時，|xi - yi| ≤ 1を満たしつつ，掛け算の結果が奇数になるのはbi = ai + 1, bi - 1の2通り考えることができる．
2. aiが奇数のときは，bi = aiの1通りである．
3. 1, 2よりaiの個数をeとすると掛け算の結果が奇数になるのは2^eと考えることができる．
4. 全ての組み合わせの個数は3^n, 奇数の組み合わせの個数は2^eなので3^n - 2^eで偶数の個数を求めることができる．
```
import itertools

n = int(input())
a = list(map(int, input().split()))
b = [i + 1 for i in a]
c = [i - 1 for i in a]

_list = []
for i in range(n):
    _list.append([a[i], b[i], c[i]])


count = 0
for comb in itertools.product(*_list):
    ans = 1
    ans2 = 0
    for c in comb:
        ans *= c
    if ans % 2 == 0:
        count += 1
print(count)

# 別解
# odd = 1
# for i in a:
#     if i % 2 == 0:
#         odd *= 2
# print(3 ** n - odd)
```
### 183C (復習)
- 解答時間
    - 40分 (調べながら解けた)
- パターン
    - いもす法，シミュレーション
- 考察
SiやTiの時刻が到達するごとに使用するお湯が増えたり減ったりするので，それぞれの時刻のタイミングでお湯を増減するように計算すればいいことがわかる．
今回は計算量が小さいので，2 * 10 ** 5の長さのリストに時刻が来るたびに増減分を付与する．そのリストの累積和をとることで，同時刻に複数人がお湯を利用している場合，全員分のその時刻におけるお湯の使用量を求めることができる．最後に累積和の各値が毎分供給しているお湯Wリットルより多いか少ないかを判定することで答えが求まる．
※計算量が多い場合は，時刻とお湯の量をハッシュテーブルに保存し，到達時刻ごとにお湯の量を増減させるようなシミュレーション的な方法もとれる．

## 計算量観点
### 73C
- 解答時間
    - 8分
- パターン
    - 計算量，dict, ハッシュテーブル
- 考察
```
joisinoお姉ちゃんが一つの数字を言うので、その数字が紙に書いてあれば紙からその数字を消し、書いていなければその数字を紙に書く。これを N 回繰り返す
```
問題として上記の条件があったので，データ構造として辞書型(ハッシュテーブル)を用意し，言われた数字をkeyとして扱い，書かれていない数字ならばTrueにし，書かれている数字であればFalseにするという2値判定をO(1)で行うことで紙に書かれている数字の個数をカウントするようにした．
```
from collections import defaultdict
n = int(input())

A = defaultdict(int)

for i in range(n):
    a = int(input())
    if not A[a]:
        A[a] = True
    else:
        A[a] = False

ans = list(A.values())
print(ans.count(True))
```
### 106C(復習)
- 解答時間
    - 解けなかった
- パターン
    - 計算量
- 考察
1以外の数字が出た瞬間に条件の文字列は無限長となり10の18乗は超える．そのため，k番目までの文字列の全てが1の場合は答えが1, それ以外の数字の場合は最初に現れた数字が答えとなる．
### 100(復習)
- 解答時間
    - 解けなかった
- パターン
    - 剰余の特性に関する問題
- 考察
× 3 を N - 1回 ÷　2を1回をN個の数列に対して行う．
この操作が行えなくなったら終了という風に考えていた．
計算量的にこの方針ではダメだった．
× 3をしても初期値として与えられる数値の÷2を行える回数は変化しない.
そのため，計算処理が必要なのは，数列の各項が÷2を何回行えるのかを求めればいい．
```
n = int(input())

A = list(map(int, input().split()))
count = 0
for i in range(len(A)):
    while A[i] % 2 == 0:
        if A[i] % 2 == 0:
            A[i] /= 2
            count += 1

print(count)

```
### ARC 108C
- 解答時間
    - 10分
- パターン
    - O(√N)問題
- 考察
n * m = pとなるn, mの組み合わせを純粋に考えると，O(N^2)となり計算時間内に間に合わない．
n * m = pとなるn, mが存在するときは, n = p // xとなるxが存在し，このxはmと考えることができる．ここでn, mを1~pまでfor文で回すことを考えると両方でn, mとm,nの組み合わせが出てくることがわかる．(2 * 3 = 6 と3 * 2 = が出現するような感じ)
よって，nは√Pまで全探索することでn * m = pとなるようなn, mを探すことができる．
そのようなn, mがあるときにn + m がsになるかを判定すればいい
```
s, p = list(map(int, input().split()))


def p_solve(p):
    i = 1
    n = []
    m = []
    while i * i <= p:
        if p % i == 0:
            n.append(i)
            m.append(p//i)
        i += 1
    return n, m

n, m = p_solve(p)

if len(n) == 0:
    print("No")
else:
    for i in range(len(n)):
        if n[i] + m[i] == s:
            print("Yes")
            exit()
    print("No")
```
### AGC 19 A (復習)
- 解答時間
    - 解けなかった(惜しかった)
- パターン
    - 貪欲法，場合分け
- 考察
0.25L, 0.5L, 1Lの1Lあたりの値段と2L換算の値段を比較して，安くなるように場合わけして料金を求めればよい．
[参考](https://img.atcoder.jp/agc019/editorial.pdf)
### 115C
- 解答時間
    - 解答できた(25分)
- パターン
    - 計算量観点
    - ソート & 大小比較
- 考察
考察1. 
最初に思いついたのは，全探索で行う方法．n, kの組み合わせで全探索を行い，各組み合わせの最小と最大の差が最も小さい値を出力するようにしていた．
しかし，これでは計算量的に問題があるのでWAを出してしまう．
考察2
選ばれた木の高さ同士の高さが近いかつの最大と最小の差が小さい値を出力できればいいので，木の高さ順にソートを行い，i番目とi+(k-1)番目の木を比較することで木の高さ同士が近い状況かつ選ばれた木の高さの最大と最小の差を小さくすることが可能になる．
この方法ならO(N)で処理を完了させることができる．
```
n, k = list(map(int, input().split()))

h = [int(input()) for _ in range(n)]
h.sort(reverse=True)
diff = 10 ** 9
for i in range(n - k + 1):
    temp_diff = h[i] - h[i + k - 1]
    diff = min(diff, temp_diff)

print(diff)
```
### 48B (復習)
- 解答時間
    - 解けなかった
- パターン
    - 集合，割り切れる数
- 考察
[参考](https://www.geisya.or.jp/~mwm48961/koukou/mobile/s1set07_m.htm)
### 131C
- 解答時間
    - 13分(復習タイム)
- パターン
    - 集合
    - 最大公倍数
- 考察
A以上B以下の数字がC, Dでも割り切れないかどうかをfor文で1つずつ調べていくのは，制約的に無理なことを認識する．
次に思いついたのは，A以上B以下の整数がC, Dで割り切れる(c_num, d_num)またはCDの最小公倍数で割り切れる(cd_num)の集合を考え，それらの数値の個数を求め，b - a (c_num + d_num - cd_num) を行えば，求められると考えた．
A以上B以下で割り切れる数字の個数は b // 割りたい数 - (a - 1) // 割りたい数で求められるので，この式を用いてc_num, d_num, cd_numを求める．
ちなみにCDの最小公倍数はgcdなどを用いて求める．
```
a, b, c, d = list(map(int, input().split()))

c_num = b // c - (a - 1) // c
d_num = b // d - (a - 1) // d

def lcm(a, b):
    import math
    return (a * b) // math.gcd(a, b)


cd_num = b // lcm(c, d) - (a - 1) // lcm(c, d)
cd_ans = c_num + d_num - cd_num

print(b - (a - 1) - cd_ans)
```
### 134C
- 解答時間
    - 解けなかった
- パターン
    - 最大値を求める問題
- 考察
自分以外の要素の中での最大値を求める．
自分より左側と右側の最大値を管理し，自分の左右の最大値同士を比較していく．
自分との比較対象が常に左側，右側の最大値になるように管理することで毎回自分以外の要素から最大値を探索する必要がなくなるため，計算量を削減することができる
```
n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

# 最初に0を入れないと1回目の
# 自分より左の最大値の管理
left = [0]
# 自分より右の最大値の管理
right = [0]

for a in A:
    left.append(max(a, left[-1]))

for a in reversed(A):
    right.append(max(a, right[-1]))

for i in range(n):
    print(max(left[i], right[n - i - 1]))
```
### 159D
- 解答時間
    - 54分
- パターン
    - 動的計画法
- 考察
今回は省略
```
from collections import defaultdict
import itertools
import math
def combinations_count(n, r):
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))


n = int(input())
A = list(map(int, input().split()))

A_count = defaultdict(int)
for a in A:
    A_count[a] += 1

select_own = defaultdict(int)
select_other = defaultdict(int)
sum_other = 0

for key, value in dict(A_count).items():
    if value - 1 >= 2:
        select_own[key] = combinations_count(value - 1, 2)
    else:
        select_own[key] = 0
    
    if value >= 2:
        select_other[key] = combinations_count(value, 2)
    else:
        select_other[key] = 0
    sum_other += select_other[key]
    

ans = 0
for a in A:
    ans = 0
    
    ans = sum_other - select_other[a] + select_own[a]
    # print(sum_other, select_other[a], select_own[a])
    print(ans)
```
### CODE FESTIVAL 2016 qual A
- 解答時間
    - 20分
- パターン
    - 対応関係
- 考察
一番簡単なのはai = j, aj = iを満たすペアを求める方法だが，O(N^2)になるので，計算量的に無理．
次に考えられるのはi番目の値がaiを好きで，ai番目のiを好きになればいいので，
key, value = value, keyのような考え方をすることができる．これは，辞書的に考えているが，list的に考えると(配列の番号, value) = (value, 配列の番号)になる．
```
n = int(input())
a = list(map(int, input().split()))

ans = dict()
for i in range(len(a)):
    ans[i + 1] = a[i]

count = 0
for i in range(len(a)):
    key = i + 1
    value = ans[key]
    if ans[value] == key:
        count += 1

if count == 0:
    count = 0
else:
    count = count // 2
print(count)
```
## 数学観点
### 55B
- 解答時間
    - 解けた(4分)
- パターン
    - mod p における割り算(合同式の性質)
- 考察
今回の問題はN!を10 ** 9 + 7で割ったときの余りを求める問題である．
しかし，単純にN!を計算し，10 ** 9 + 7で割ると数値が大きくなっている場合，
オーバーフローが発生する．そのため合同式の積の性質を用いて問題を解けばいい.
例： 10 ≡ 3 mod 7は10 % 7と3 % 7の余りの値が同じという性質を表している．
これに合同式の積の性質を用いて考えると, 30 ≡ 9 mod 7はどちらも余りが２となり，
余りが一致していることがわかる．よって求める値は, ans * i ≡ (ans * i mod 10 ** 9 + 7) mod (10 ** 9 + 7)ということになる. これによりN!倍していく過程において常に小さい値で演算を行えるので，オーバーフローが発生しない．
```
n = int(input())

ans = 1
for i in range(1, n + 1):
    ans = ans * i % (10 ** 9 + 7)
print(ans % (10 ** 9 + 7))

```
### 60B
- 解答時間
    - 20分
- パターン
    - 数列
    - 余り, 倍数
- 考察
[参考](https://img.atcoder.jp/arc073/editorial.pdf)
### 88C (復習)
- 解答時間
    - 解けなかった
- パターン
    - 変数，式変形
- 考察
純粋に変数を定義して，問題を解けばよかった．
変に色々と複雑に考えすぎて，逆に解けなかった．
### 69C (復習)
- 解答時間
    - 解けなかった
- パターン
    - 数字の特性
- 考察
2の倍数と4の倍数がどのような並びの時に，a<= i <= N - 1について, a_iとa_i+1の積が4の倍数になるのかを考える．
2の倍数と4の倍数がAの中に何個入っていれば，条件を満たすようになるのかを考えればいい．
- 感想
2の倍数で割れる数の個数や4の倍数で割れる個数を数えて，考えるというところまではたどり着いたが，その後, 具体的に例を挙げることができていなかった．
### 70C
- 解答時間
    - 5分
- パターン
    - 最小公倍数
- 考察
様々な速度で時計を一周する時計の針が同一のタイミングで真上を向くタイミングを問う問題である．これは言い換えると全ての値が同じ値を取り得る最小の倍数でなければならないので，最小公倍数を求めればいいことがわかる．
```
# 5分
import math
def lcm(x, y):
    import math
    return (x * y) // math.gcd(x, y)

n = int(input())
T = [int(input()) for _ in range(n)]

lcm_num = T[0]

for t in T[1:]:
    lcm_num = lcm(lcm_num, t)
print(lcm_num) 
```
### 93C(復習)
- 解答時間
    - 解答できなかった
- パターン
    - 数の偶奇の性質の考察
- 感想
    - 実装の取っ掛かりすら，思いつけてなかった．制約条件が行われた時の数の性質について考察を深める必要がある．
- 考察
今回の2種類の操作ではどちらも総和として+2になるので操作前と操作後で総和の偶奇は変化しない．
そのため，総和の偶奇が一致している場合は操作後の総和であるmax(a, b, c) × 3から操作前の(a + b + c) の差を÷2した数が操作回数となる．(1操作で総和は2変化するので2で割っている．)一方，総和の偶奇が一致しない場合は， a, b, cを合わせるための基準となる最大値max(a, b, c)を+1して(下げる操作はないため)，偶奇が一致するように最大値を再設定する必要がある．そのため偶奇が一致しないときは(max(a ,b, c) + 1) × 3から(a + b + c)の差を÷2した数が操作回数となる.
```
A, B, C = map(int, input().split())

M = max(A, B, C)

if 3 * M % 2 == (A + B + C) % 2:
    print((3 * M - (A + B + C)) // 2)

else:
    print((3 * (M + 1) - (A + B + C)) // 2)
```
### 103C
- 解答時間
    - 15分
- パターン
    - 最小公倍数
- 考察
mを割るときの余りの最大値は割る数である数列aiより1小さい数字であることがわかる．各項毎にmは異なることなく共通であることを考えると，aiの最小公倍数から1小さい数字がmと考える事ができる．
```
(公式の解説)
m = a1 × a2 × · · · × aN とすると、各 i について m mod ai = 0 なので、(m − 1) mod ai = ai − 1 です。
したがって f(m − 1) = (a1 − 1) + (a2 − 1) + · · · + (an − 1) となり、各項が最大値を取っているのでこれが
f の最大値です。実装では、m は非常に大きいため、m を計算せずに f(m − 1) を直接計算すればよいです。
よって、O(n) でこの問題が解けました。

```
```
import math

def lcm(x, y):
    
    return (x * y) // math.gcd(x, y)

n = int(input())

A = list(map(int, input().split()))

lcm_val = A[0]
for i in range(1, len(A)):
    lcm_val = lcm(lcm_val, A[i])

ans = 0

for i in range(len(A)):
    ans += (lcm_val - 1) % A[i]
print(ans)
```
### 109C
- 解答時間
    - 8分30秒
- パターン
    - 最小公倍数
- 考察
この問題では，Xから与えられた地点までの距離へ行くために±Dしか勧めない制限がかけられている．そのため，最小で到達できる距離と最大で到達できる距離が倍数の関係になっていなければならないことがわかる．
そのため，Xと与えられた地点の距離を算出し，それらの距離の最小公倍数となる値を求めればいい．
```
# 8分半
import math

n, X = list(map(int, input().split()))
x_list = list(map(int, input().split()))

min_val = min(x_list)

diff = []
for x in x_list:
    _diff = abs(X - x)
    if _diff == 0:
        _diff = 2
    diff.append(_diff)
# print(diff)

gcd = diff[0]
for i in range(1, len(diff)):
    gcd = math.gcd(gcd, diff[i])

print(gcd)
```
### 133C (復習)
- 解答時間
    - 解けなかった
- パターン
    - 剰余の特性
- 考察
[参考](https://img.atcoder.jp/abc133/editorial.pdf)
i * j mod 2019で最小値として考えられるのは，0 ~ 2018の間の値となる．
i, jのどちらかがl ~ ｒ間に2019に近い数字の倍数を見つけることができれば，小さい値の余りを見つけることができることからi, jが2 ~ 2019までの倍数である数字を見つけ出せばいい．よってl ~ min(l + 2019, r + 1)の間から2つの数字の組み合わせの掛け算の結果と2019との余りをとることで全探索で余りの最小値を探すことができる．
### 140C
- 解答時間
    - 解けなかった
- パターン
    - 数列の問題(最大値を取り続ける)
- 考察
数列関係の問題は見ただけですぐに理解しにくいので，実際の値を書き出してみて，
パターンがありそうか観察してみること．(具体化 -> 一般化)
- 考察: [解説記事](https://drken1215.hatenablog.com/entry/2019/09/16/201500)
- 数列の前後の関係性に注目する()
### 171C
- 解答時間
    - 解けなかった
- パターン
    - 進数
- 考察
この問題では，与えられた数値に対して
```
1,2,⋯,26 番の番号がついた犬はその順に a,b,...,z と命名されます。
27,28,29,⋯,701,702 番の番号がついた犬はその順に aa,ab,ac,...,zy,zz と命名されます。
703,704,705,⋯,18277,18278 番の番号がついた犬はその順に aaa,aab,aac,...,zzy,zzz と命名されます。
18279,18280,18281,⋯,475253,475254 番の番号がついた犬はその順に aaaa,aaab,aaac,...,zzzy,zzzz と命名されます。
475255,475256,⋯ 番の番号がついた犬はその順に aaaaa,aaaab,... と命名されます。
```
のような条件で文字列に変換するように処理を行う必要がある．
このような数値の変換は，26進数と考えることができる．
26で繰り上がる度に文字数が増え，26からの+の数値分だけアルファベットが進んでいることから見てわかる．
26進数では最後の数値は25となるので，n番目に対応する文字はn = n - 1で初期化を行い，chr(ord('a') + n % 26)したものになる．
1~26番目は0~25となるのでord('a')を足している．この処理を行うことで1の位でも対応できる
[参考](https://drken1215.hatenablog.com/entry/2020/06/21/225500)
## カテゴリ観点
### 90C (復習)
- 解答時間
    - 解けなかった
- パターン
    - 場合分け
- 考察
カードが裏になるのは，カードをめくる回数が奇数回のときなので，めくる回数が奇数回となる場所を考える．
1. n = 1, m= 1のときはめくるのは1回なので，1
2. n = 1, m != 1のとき，両端は2回，その間は3回めくられるので，(m - 2)
3. n >= 2, n <= m, m >= 2のとき，四隅がめくられるのは4回，周上をめくられるのは6回，それ以外は9回めくられるので，奇数回めくられるのは(n - 2) * (m - 2)となる． 
### 96C(復習)
- 解答時間
    - 解けなかった
- パターン
    - '#', '.'を使う系のマス目の問題
    - あまり得意でない
- 考察なし
問題文の意味を読み取れていなかった
このパターンの問題は現在地からx, y方向に+1, -1したときの場所の存在の有無を確認するチェック関数が必要となる．

### AGC 3 A
- 解答時間
    - 15分
- パターン
    - 場合分け
- 考察
北西南東に進んでN日間旅して家に戻ってこれるかどうか．
条件として1日にどれだけの距離を移動してもいいことになっているので，方角が対極になっている方角同士の組み合わせが1度でも存在するような旅程は家に戻ってくることができる．
要するに，北南と西東と北西南東に進むこの3パターンのみが帰宅できるパターンである．
距離はいくらでも移動できるので，このパターンが一度でも出るかを判定し，出る場合はYes, 出ない場合はNoとすればいいだけ．
```
s = input()

num = len(set(s))


if num == 1:
    print("No")
elif num == 2:
    n = s.count('N')
    e = s.count('E')
    w = s.count('W')
    S = s.count('S')
    if n >= 1 and S >= 1:
        print("Yes")
    elif e >= 1 and w >= 1:
        print("Yes")
    else:
        print("No")
elif num == 4:
    print("Yes")
else:
    print("No")

```

### AGC 40 A (復習)
- 解答時間
    - 解けなかった
- パターン
    - 左右の文字の数による考え方
- 考察
[参考](https://img.atcoder.jp/agc040/editorial.pdf)

### AGC 12 A
- 解答時間
    - 19分
- パターン
    - 値の取り方の法則の見極め
- 考察
チームを組んだ時にチーム内で2番目の強さがチームの強さとして表される．このとき全チームの強さが最大になるようなチームの組み方を求める．
最初に考えた方法は，ソートして1~n, n+1~2n, 2n+1~3nの三組に分割して，それぞれから1, 2, 3番目と強い順位チームを組ませる方法を考えた．これでは，うまくいかない．
例：1 1 1 1 5 6となっているとき，上記の方法だと(1, 1, 5), (1, 1, 6)となり総和が2になってしまう．(本当は(1, 5, 6), (1, 1, 1)で6が理想)
次に考えたのが，ソートして後ろから2番目ずつをとる方法．すべての組の2番目の大きさが2番目として選べる最大であるためには，自分より大きい値が最低1つあればいいので，最低1つがある状況を考えると後ろから1飛ばしずつとった値が2番目に選べる数値として最大の数を選んでいることになる．
```
n = int(input())
a = list(map(int, input().split()))

a.sort()
# print(a)
ans = 0
for i in range(n):
    ans += a[n + 2 * i]
print(ans)
```