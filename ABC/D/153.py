# 20分
# 方針: 実際に値が減っていく方法を書いていく
# 与えられた数値を2で割っていくと，演算回数が2 ** (n + 1) - 1になっていることがわかる
# そのため答えは与えられたhを2で割れる回数を求めて，-1をすれば求まる
# HACK 再帰処理も使える

h = int(input())

n = 0
while h > 0:
    h = h // 2
    n += 1

ans = 2 ** n - 1
print(ans)