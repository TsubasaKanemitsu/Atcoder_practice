# 考察がもう1ステップ足りなかった

# 考察ステップ
# DFSでやるということ
# 計算量は見積もって 3 *  10 ** 6であること
# 重複順列であればいいこと

# 次に選べる文字がどのような特性を持つかを
# 明確化することができていなかった.

import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

std = 97

def dfs(word, i):
    if len(word) == n:
        print(word)
        return
    max_word = max(word)
    # 次に追加できる文字は，これまでに出現した文字より
    # 1つ上の文字列
    # a ~ これまでに出現した文字の中で最大の文字 + 1
    lim = ord(max_word) - (std - 1)
    for j in range(lim + 1):
        dfs(word + chr(j + std), j)


dfs('a', 0)
