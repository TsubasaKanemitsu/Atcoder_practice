N = int(input())

ans = 0

# 数nについて調べ，末尾に数字を追加した数を再帰的に調べる関数
# use3, user5, user7

# 再帰的に末尾に3, 5, 7を追加していくところがミソ

def dfs(n, use3, use5, use7):
    global ans
    # Nを超えていたら打ち切って終了する
    if n > N:
        return

    # 3種類全てを使っていたら答えに加算する
    if use3 and use5 and use7:
        ans += 1
    
    # 末尾に3, 5, 7をつけた数を再帰的に調べる
    # 末尾に数字を加えるということは，10倍されるかつ3 or 5 or 7
    dfs(10 * n + 3, True, use5, use7)
    dfs(10 * n + 5, use3, True, use7)
    dfs(10 * n + 7, use3, use5, True)


dfs(0, False, False, False)

print(ans)