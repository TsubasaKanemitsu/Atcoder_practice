x, n = list(map(int, input().split()))
P = list(map(int, input().split()))
num = 0
while True:
    if not x - num in P:
        ans = x - num
        break
    if not x + num in P:
        ans = x + num
        break
    num += 1
print(ans)


# 差の最小値を見つけるということは
# 差の大きさを0から順に増やしていきそれに一致する値があるかを探索すればいい
# 差を可変にして探索
# 自分は，Pに存在しない値を可変にして探索していた