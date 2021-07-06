N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N):
    t = 0
    for j in range(i, N - 1):
        c, s, f = CSF[j]
        # 始発に乗れるなら乗る
        if t < s:
            t = s
        # 列車はf秒おきに出発しているので、出発時に丁度ついたときは、すぐに乗れる
        elif t % f == 0:
            pass
        # ついたのが丁度ではない場合、待ち時間が発生する
        else:
            t = t + f - t % f
        t += c
    print(t)