n, m = list(map(int, input().split()))
K = []
S = []
for i in range(m):
    input_list = list(map(int, input().split()))
    K.append(input_list[0])
    S.append(input_list[1:])
P = list(map(int, input().split()))

ans = 0
# スイッチの光り方
for bit in range(1 << n):
    on_light = 0
    # 電球ごと
    for i in range(m):
        on_switch = 0
        for s in S[i]:
            # 光っているスイッチがS[i]の中に存在しているとき
            if bit & (1 << s - 1):
                on_switch += 1
        if on_switch % 2 == P[i]:
            on_light += 1
    if on_light == m:
        ans += 1
print(ans)