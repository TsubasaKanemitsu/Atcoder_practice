# 二分探索
# ある値までに存在する値の個数のメモ化

# 値の個数の圧縮
# 単調増加する値の個数
# ある値までの最大のi

# ある値までに存在している良い整数の個数がわかれば，
# あとはある値 + (k - ある値までに存在している良い整数の個数)で
# 現在の良い整数を求めることができる

import bisect
n, q = list(map(int, input().split()))

A = list(map(int, input().split()))

# Aiまでの良い整数の個数を計算
C = [A[i] - (i + 1) for i in range(n)]
k = [int(input()) for _ in range(q)]

for i in range(q):
	K = k[i]
	r = bisect.bisect_left(C, K)
	# K番目までの良い整数を持つ値の位置を求める
	# AiまでにK番目までの良い整数がある
	if r == 0:
		print(K)
	else:
		# Ai-1からAi番目までの間にK番目の良い整数が存在している
		# その値はi - 1番目のAiの値からAi-1までに存在している良い整数の個数を引いた数の個数分だけ
		# Aiに足し合わせたものになる．
		print(A[r - 1] + (K - C[r - 1]))
