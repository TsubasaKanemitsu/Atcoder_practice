# 22 ~ 3分
# 絶対値の最小の差
# クラスのレーティングをソートして左隣と右隣の値が，生徒の適正レーティングの
# 近傍の値となるので，そのどちらかの小さい方の差を出力する

# キーワード
# 要素の検索はソートして二分探索
# 一致する要素や最も近い要素の検索は二分探索

import bisect
n = int(input())
A = list(map(int, input().split()))
q = int(input())
B = [int(input()) for _ in range(q)]

A.sort()
len_a = len(A)
ans = []
for i in range(q):
    index = bisect.bisect_left(A, B[i])
    diff1 = 10 ** 99
    diff2 = 10 ** 99
    if index < n:
        diff1 = abs(A[index] - B[i])
    if index >= 1:
        diff2 = abs(A[index - 1] - B[i])
    print(min(diff1, diff2))