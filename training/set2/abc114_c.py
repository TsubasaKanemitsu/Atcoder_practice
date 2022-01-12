# 10min
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())


ans = 0

def dfs(v):
    global ans
    if v > n:
        return
    v = str(v)
    if v.count('3') >= 1 and v.count('5') >= 1 and v.count('7') >= 1:
        ans += 1

    dfs(int(v + '3'))
    dfs(int(v + '5'))
    dfs(int(v + '7'))


dfs(3)
dfs(5)
dfs(7)
print(ans)

# テクニック
# 桁を上げるで数字を追加するときに
# 数値を文字列化して、数字を文字列として足すこととs
# 10倍して追加したい数字を足すのと同じ