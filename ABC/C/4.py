# 40分
# 問題の意味を理解してからは20分

from collections import deque
n = int(input())
list_n = deque([str(i) for i in range(1, 7)])

# 入れ替え回数は5回なので，先頭を末尾まで入れ替え続けることができる回数を求める
# これだけでは，先頭が末尾まで行く入れ替えを何回も同じことを行うことになるので
# 周期性を利用してい考える．具体的には，先頭が末尾まで入れ替えれた場合のパターンは
# 全部で6パターンあるため，先頭から末尾までの入れ替え可能数のmodをとれば，周期性を
# 数値化できる．

syou = n // 5 % 6
# 先頭から末尾の途中までしか入れ替えれない部分がmodとなる．
mod = n % 5

# 入れ替えをn回するときに先頭から末尾までを入れ替えれる最後の状態にする処理
for i in range(syou):
    num = list_n.popleft()
    list_n.append(num)

# 先頭から末尾まで入れ替えた後に，先頭から末尾の途中までしか入れ替えれない
# 残りの入れ替え作業を行う処理
list_n = list(list_n)
for i in range(mod):
    num = list_n[i]
    list_n[i] = list_n[i + 1]
    list_n[i + 1] = num

print(''.join(list_n))