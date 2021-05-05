# 最大値の最小化, 数列の性質
# 奇数と偶数番目に出現する文字数をカウントする
# 奇数番目と偶数番目において出現回数の多い文字数の
# 候補の上位2番目までをそれぞれ列挙する．(1番目が被ることがあるから)
# それらの組み合わせの中で出現回数が最大になるものを選ぶ
# ここで選んだ組み合わせは変更する必要のない文字なので，
# これらの合計文字数を全文字数から引いた値が変える必要のある文字数となる．
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

odd_cnt = defaultdict(int)
even_cnt = defaultdict(int)
for i in range(n):
    if i % 2 == 0:
        odd_cnt[A[i]] += 1
    elif i % 2 == 1:
        even_cnt[A[i]] += 1

odd = []
even = []
for k, v in odd_cnt.items():
    odd.append([k, v])
for k, v in even_cnt.items():
    even.append([k, v])

odd.sort(key=lambda x:x[1], reverse=True)
even.sort(key=lambda x:x[1], reverse=True)

# 文字一種類
if len(set(A)) == 1:
    print(n // 2)
    exit()

# 文字2種類以上
if len(odd) > 1:
    odd = odd[0:2]
if len(even) > 1:
    even = even[0:2]

sm = 0
for k, v in odd:
    for kk, vv in even:
        if k!= kk:
            sm = max(sm, v + vv)
print(n - sm)