n, m = list(map(int, input().split()))

K = []
S = []
for i in range(m):
    _input = list(map(int, input().split()))
    K.append(_input[0])
    S.append(_input[1:])
p = list(map(int, input().split()))

count = 0
# bitで0, 1での表し方の全通り
for bit in range(1 << n):
    flush_lamp = 0
    for i in range(m):
        on_switch = 0
        for s in S[i]:
            # s - 1になるのは，ビットでは0乗, 1乗, 2乗という風に
            # 増えていくので，スイッチがs[i]番目のをそのままビット演算に
            # 使用すると1乗分余分なことになるのでs - 1にする必要がある．
            if bit & (1 << s - 1):
                on_switch += 1
        if on_switch % 2 == p[i]:
            flush_lamp += 1
    if flush_lamp == m:
        count += 1

print(count)

# スイッチONパターンをビット列の全通りで表す
# 特定のスイッチONパターンにおいて，M行の
# スイッチの配置パターンがそれぞれ必ずランプを
# 光らせることができるのかを判定する．