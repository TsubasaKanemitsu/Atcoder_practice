# Rain Flows into Dams
# 貪欲法、漸化式
# 前の状態が決まれば、次の状態がきまる。

# 各ダムの水がたまる状態に関する立式を行う
# A1 = X1 + X2
# A2 = X2 + X3
# ...
# その結果
# 2X1 = A1 - A2 + A3 + - A4 + ...
# という風に値が決まる
# 2X1 の値が求まれば、残りは最初に立式していた
# A2 = X2 + X3に2X1を代入することを考えると
# 2A2 = 2X2 + 2X3
# 2X2 = 2A1 - 2X1となり
# 2X2を求めることができる
# これを2Xnまで求めることで各山iに降った水の量を求めることができる。

n = int(input())
A = list(map(int, input().split()))

x = 0
for i in range(n):
    if i % 2 == 0:
        x += A[i]
    else:
        x -= A[i]

ans = [x]
for i in range(n - 1):
    x = 2 * A[i] - x
    ans.append(x)
print(*ans)