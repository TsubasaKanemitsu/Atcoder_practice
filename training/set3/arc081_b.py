# 自力AC
# 1時間
n = int(input())
S = [list(input()) for _ in range(2)]
MOD = 10 ** 9 + 7
# 1列目のドミノ
# 縦ドミノ
ans = 0
now = 0
shape = 'tate'
if S[0][0] == S[1][0]:
    ans = 3
    now = 1
    shape = 'tate'
# 横ドミノ
else:
    ans = 6
    now = 2
    shape = 'yoko'
while now < n:
    # 縦ドミノ
    if S[0][now] == S[1][now] and shape == 'tate':
        ans *= 2 % MOD
        now += 1
        shape = 'tate'
    elif S[0][now] != S[1][now] and shape == 'tate':
        ans *= 2 % MOD
        now += 2
        shape = 'yoko'
    # 横ドミノ
    elif S[0][now] == S[1][now] and shape == 'yoko':
        ans *= 1 % MOD
        now += 1
        shape = 'tate'
    elif S[0][now] != S[1][now] and shape == 'yoko':
        ans *= 3 % MOD
        now += 2
        shape = 'yoko'
print(ans % MOD)


# 考察1 初期状態の設定
# 縦ドミノの時は3パターン
# a
# a

# 横ドミノが縦に2つ並ぶときは6パターンとなる
# b b
# c c

# 考察2 前後のドミノの関係性に着目する
# 次のドミノが選ぶことができる色は
# 1つ手前のドミノの状態に依存する

# pattern1
# 以下のような縦のドミノは二つ並んでいる場合
# a b
# a b
# bのドミノは2色選べる

# pattern2
# 以下のような縦のドミノと横のドミノが二つ並んでいる場合
# a b b
# a c c

# b b
# c c
# の色の組み合わせは2通りとなる

# pattern3
# 横ドミノが4つ並んでいる場合
# a a c c
# b b d d

# c c
# d d
# の色の組み合わせは3通りとなる

# pattern4
# 横ドミノが2つと縦ドミノが並んでいる場合
# a a c
# b b c

# c のドミノは1色選べる

# 上記4パターンの判定に応じた通り数を掛け算していくことで
# 組み合わせの総数を求めることができる
