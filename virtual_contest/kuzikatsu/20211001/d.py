# 数え上げ問題
# 固定化して考える

n = int(input())

# ペアリングの個数を数えるときの考察でよくあるのが、
# Aを固定し、それに応じたBが何個あるのかを高速に数え上げる方法
# Aを固定したときのBの個数は、Aの「最上位の値」と「1の位」のみに依存する

num = [[0] * 10 for _ in range(10)]
for i in range(1, n + 1):
    number = str(i)
    a, b = int(number[0]), int(number[-1])
    if b != 0:
        num[a][b] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += num[i][j] * num[j][i]
print(ans)