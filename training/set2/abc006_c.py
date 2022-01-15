# 復習

# 値の固定化
# 計算高速化

n, m = list(map(int, input().split()))

# 鶴亀算みたいな問題
# 3つの変数が存在しているので
# このうちの1つを固定化して、O(M^2)になる愚直解を
# O(M)にしたい

for a in range(m // 2 + 1):
    # 老人0人
    pattern1 = m - 2 * a
    c = pattern1 // 4
    if pattern1 % 4 == 0 and a + c == n:
        print(a, 0, pattern1 // 4)
        exit()
    # 老人11人
    pattern2 = (m - 3) - 2 * a
    c = pattern1 // 4
    if pattern2 % 4 == 0 and a + c + 1 == n:
        print(a, 1, pattern2 // 4)
        exit()
print(-1, -1, -1)