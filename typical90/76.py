# 典型90問
# 76 ★3
# 尺取り法, 二分探索 + 累積和
# 連続するピースなので、Nと1を連続することを考えると、Aを連結させて2N番目までの配列として考えるのが良い.

# 考察テクニック
# 区間管理としてleft, rightを用意する
# 連続区間の選び方として、始端と終端を連続させるために配列を連結する

# O(N)で解くことができる

# 実装テクニック
# 左と右のフラグが被ったときの処理
# 左右のフラグの終端処理
# 左だけを進める、右だけを進める処理
# などを考える必要がある

n = int(input())
A = list(map(int, input().split()))
all_a = sum(A)
A.extend(A)

left = 0
right = 0

num = 0

while True:
    # 10分の1を超えるまで
    while num <= all_a / 10 and right < 2 * n:
        num += A[right]
        right += 1
        if num == all_a / 10:
            print("Yes")
            exit()
        # print("N", left, right, num)
    if left == right:
        num += A[right]
        right += 1
        
    else:
        num -= A[left]
        left += 1
    # print("N", left, right, num)    
    if left == 2 * n and right == 2 * n:
        print("No")
        exit()
    