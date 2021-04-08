# 15分
n = int(input())
c = list(input())

red = c.count('R')
white = c.count('W')

# 仕切りを作る
div_line = red
# 仕切りより左側の白色と右側の白色のうち，多い方の数だけ操作が必要となるので
ans = max(c[:div_line].count('W'), c[div_line:].count('R'))
print(ans)