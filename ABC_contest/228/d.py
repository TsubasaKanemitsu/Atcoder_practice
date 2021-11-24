q = int(input())
TX = [list(map(int, input().split())) for _ in range(q)]

n = 2 ** 20
A = [-1] * n

for i in range(len(TX)):
    t, x = TX[i]
    if t == 1:
        h = x
        Ah_mod_n = h % n
        # 高速化が必要
        # hから最短でたどり着けるインデックスを探索する(値が-1のところ)
        # 探索がわからん
        while A[Ah_mod_n - 1] != -1:
            h += 1
            Ah_mod_n = h % n
        A[Ah_mod_n - 1] = x
    elif t == 2:
        print(A[x % n - 1])
