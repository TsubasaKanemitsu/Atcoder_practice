a, b = list(map(int, input().split()))

w_a = a // 100
w_b = b // 100
s_a = int(str(a)[1])
s_b = int(str(b)[1])
t_a = int(str(a)[2])
t_b = int(str(b)[2])


if w_a == 9 and w_b == 1 and (s_a != 9 or s_b != 0):
    if 9 - s_a >= s_b:
        ans = a + 10 * (9 - s_a) - b
    else:
        ans = a - (b - s_b * 10)
elif w_a == 9 and w_b == 1 and s_a == 9 and s_b == 0:
    if 9 - t_a >= t_b:
        ans = a + (9 - t_a) - b
    else:
        ans = a - (b - t_b)
else:
    if 9 - w_a >= w_b - 1:
        ans = a + 100 * (9 - w_a) - b
    else:
        ans = a - (b - (w_b - 1) * 100)
print(ans)