# 20分
# 1WA

# 条件にあう要素が同じ数以上あるかを知りたい
# ハッシュテーブルで要素数をカウントしておけば
# すぐに条件に一致するかどうかを判定することができる
# 要素の順番にとらわれない問題ではハッシュテーブルは使える
# 一致する要素が条件を満たしているか判断するのもO(1)なので早い


from collections import Counter
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d_cnt = Counter(d)
t_cnt = Counter(t)

for k, v in t_cnt.items():
    if d_cnt[k] < v:
        print("NO")
        exit()
print("YES")

