# 4分半
a, b, k = list(map(int, input().split()))

if a > k:
    print(a - k, b)
else:
    print(0, max(b + a - k, 0))

# 考察
# 制約としてKは10^12なので，全探索で問題文通りにクッキーを減らしていくことは計算量的に無理だと考える
# 次に場合分けして，aとbの値を求める
# patter1: a > k の場合は高橋君はk個だけクッキーを食べるので，a - k個残る．青木君のクッキーは減らないのでb個残る
# pattern2: k > aの場合，k > a + bとa + b > k >aの2通りが考えれる．
# このとき，高橋君のクッキーは全てなくなるので0個，青木君はこの2通りのうちの最大となる方が残るクッキーの個数なのでmax(0, a + b - k)と考えることができる

