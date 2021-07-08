# 少し詰まる
# 時間掛かりすぎ
# シミュレーション
# 21分21

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
monster = 0
for i in range(n):
    # 倒す数
    monster = B[i] - A[i] - A[i + 1]
    if monster < 0:
        ans += B[i]
        if B[i] - A[i] > 0:
            A[i + 1] -= B[i] - A[i]
    else:
        ans += A[i] + A[i + 1]
        A[i + 1] = 0
print(ans)
