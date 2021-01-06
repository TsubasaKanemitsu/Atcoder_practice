A, B, C, X, Y = list(map(int, input().split()))
money = 10**10
for i in range(10**5 + 1):
    money = min(money, 2 * C * i + A * max(X - i, 0) + B * max(Y - i, 0))
    
print(money)

# 全探索 いい例
# やり直し
