v, t, s, d = list(map(int, input().split()))

ss = d / v
if t <= ss <= s:
    print("No")
else:
    print("Yes")