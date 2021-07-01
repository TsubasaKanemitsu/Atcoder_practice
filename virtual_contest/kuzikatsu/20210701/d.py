# https://drken1215.hatenablog.com/entry/2020/04/05/150900
import sys
sys.setrecursionlimit(10 ** 7)

K = int(input())

def dfs(d, val, ans):
    ans.append(val)

    if d == 10:
        return
    
    for j in [-1, 0, 1]:
        # valの最後の1桁 + -1 ~ 1
        add = (val % 10) + j
        # 追加する値が0から9に収まるときだけ (= 絶対差が±1になるときだけ)
        if add >= 0 and add <= 9:
            # 桁を1つ上げる
            dfs(d + 1, val * 10 + add, ans)

ans = []

for i in range(1, 10):
    dfs(1, i, ans)

ans.sort()
print(ans[K - 1])
