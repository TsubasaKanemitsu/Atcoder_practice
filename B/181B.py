N = int(input())

sm = 0
for i in range(N):
    A, B = list(map(int, input().split()))
    sm += B * (B + 1) / 2 - A * (A - 1) / 2
print(int(sm))

# 計算量を意識する
# 数列の総和の計算式を上手く利用し，ACに収まる計算量にする