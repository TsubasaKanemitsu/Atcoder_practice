import math

# 考察
# STEP1
# Nは1 <= N <= 10 ** 12なので全探索は無理
# STEP2
# floor(a * x / b)を最大化し、floor(x / b)を最小化するには
# xを最大化しつつ、xをb未満にできればいい
# そうすることで右側の式は0にすることができ
# 左側の値を最大値とすることができる

a, b, n = list(map(int, input().split()))

if n >= b:
    x = b - 1
else:
    x = n

ans = math.floor(a * x / b) - a * math.floor(x / b)
print(ans)