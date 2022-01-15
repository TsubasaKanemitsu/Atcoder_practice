import sys
sys.setrecursionlimit(10 ** 7)
a, n = list(map(int, input().split()))

# 操作A
# xを黒板から消して、a * x

# 操作B 条件付き
# x >= 10 かつ x % 10 != 0のときのみ
# xの末尾の文字を先頭に持ってくる
# 例： 123 -> 321

# 考察

# 1 -> Nにすることができない場合
# aがNより大きい場合
# 操作A
# 1 * a > Nになるため -1
# 操作B
# x < 10なので -1



if a > n:
    print(-1)
    exit()

# 逆に戻していく方法はあるか?

flag = False
cnt = 0
ans = 0
visited = [[False, False] for _ in range(n + 1)]

def dfs(v):
    global ans
    global cnt
    global flag
        
    if (visited[v][0] * visited[v][1]):
        return

    # print(v)
    if v == 1:
        flag = True
        ans = cnt
        return

    # 操作A
    if v % a == 0:
        if not visited[v][0]:
            visited[v][0] = True
            cnt += 1
            v = v // a
            dfs(v)
            cnt -= 1
            v = v * a

    # if visited[v]:
    #     return
    # print("v1", v)
    # 操作B
    if v >= 10 and v % 10 != 0:
        v = list(str(v))
        temp = v[0]
        v[0] = v[-1]
        v[-1] = temp
        v = int(''.join(v))
        if not visited[v][1]:
            visited[v][1] = True
            cnt += 1
            dfs(v)
            cnt -= 1
    return

dfs(n)
if flag:
    print(ans)
else:
    print(-1)
