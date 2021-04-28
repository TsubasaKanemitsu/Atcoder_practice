n = int(input())
L = list(map(int, input().split()))

mx_l = max(L)

L.remove(mx_l)
sm_l = sum(L)

if mx_l < sm_l:
    print("Yes")
else:
    print("No")