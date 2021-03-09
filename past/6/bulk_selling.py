# from collections import Counter
n = int(input())

c = list(map(int, input().split()))
# c_cnt = Counter(int)

q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]

z = 0
s = 0

min_set_sell = 10 ** 9 + 1
min_all_sell = 10 ** 9 + 1

# セット販売，
for i in range(n):
    # セット販売のCの最小値
    if i % 2 == 0:
        min_set_sell = min(c[i], min_set_sell)
    # セット販売以外のCの最小値
    else:
        min_all_sell = min(c[i], min_all_sell)

ans = 0

for i in range(q):
    num = query[i][0]
    if num == 1:
        x = query[i][1] - 1
        a = query[i][2]
        # セット販売とセット販売以外による販売枚数は変数として持つ
        # 最後にO(N)で値の更新を行えるように，各時点での販売可能枚数を更新していく
        # min_set_sell, min_all_sellにはs, zので引かれた分は考慮されていないので，
        # 2, 3の各処理内で単品で販売した枚数に追加するようにして
        # セット販売とセット販売以外による販売枚数を調節する

        # セット販売対象
        if x % 2 == 0:
            card = c[x] - s - z
        # セット販売以外対象
        else:
            card = c[x] - z

        if card >= a:
            c[x] -= a
            ans += a
            if x % 2 == 0:
                min_set_sell = min(c[x], min_set_sell)
            else:
                min_all_sell = min(c[x], min_all_sell)

    elif num == 2:
        a = query[i][1]
        if min_set_sell - s - z >= a:
            s += a
    
    else:
        a = query[i][1]
        if min(min_all_sell - z, min_set_sell - s - z) >= a:
            z += a

for j in range(n):
    if j % 2 == 0:
        ans += s
    ans += z
print(ans)