x, k, d = list(map(int, input().split()))
x = abs(x)
# k回移動しても0にたどり着けない場合
if x > k * d:
    print(x - k * d)
    exit()

else:
    # 距離Xの中で距離Dを移動できる回数
    cnt = x // d

    # 移動回数がちょうどk回
    if cnt == k:
        print(0)
        exit()

    k = k - cnt
    if k % 2 == 1:
        print(abs(x - d * (cnt + 1)))
    else:
        print(abs(x - d * cnt))
