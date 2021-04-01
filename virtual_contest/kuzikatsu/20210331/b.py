n, a, b = list(map(int, input().split()))

diff = abs(a - b)
if diff % 2 == 0:
    round_n = diff // 2
else:
    # diff1 = max(a, b) - 1
    # diff2 = n - min(a, b)
    # round_n = min(diff1, diff2)

    # 左端までの移動(a, b間の距離が偶数になるための距離)
    move_left = min(a, b)
    round_ln = (max(a, b) - move_left - 1) // 2 + move_left

    # 右端までの距離(a, b間の距離が偶数になるための距離)
    move_right = n - max(a, b) + 1
    round_rn = (n - (min(a, b) + move_right)) // 2 + move_right

    round_n = min(round_ln, round_rn)

print(round_n)